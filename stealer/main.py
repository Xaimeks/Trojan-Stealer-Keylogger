import os
import socket

def send_file(file_path, server_ip, server_port):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.socket((server_ip, server_port))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break

            client_socket.sendall(data)

    client_socket.close()

send_file('путь к файлу', 'айпи вашего сервера', 'порт вашего сервера')