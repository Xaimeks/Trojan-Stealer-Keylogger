import socket

def send_file():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind('0.0.0.0', 1234)
    server_socket.listen(1)
    print('Ожидаем подключения')

    client_socket, client_address = server_socket.accept()
    print(f'Подключено {client_address}')

    with open('file_to_send.txt', 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print('Файл отправлен')
    client_socket.close()
    server_socket.close()

send_file()