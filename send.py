import os
import socket

def send_file(file_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                s.send(data)
                data = file.read(1024)

def monitor_directory(directory_path, host, port):
    while True:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        if files:
            for file_name in files:
                file_path = os.path.join(directory_path, file_name)
                print(f"Sending {file_name} to {host}:{port}")
                send_file(file_path, host, port)
                os.remove(file_path)
                print(f"{file_name} sent and deleted.")

if __name__ == "__main__":
    directory_to_monitor = "D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\translated audio" # Replace with the directory you want to monitor
    target_host = "127.0.0.1"  # Replace with the target machine's IP address or hostname
    target_port = 12345  # Change to your desired port number

    monitor_directory(directory_to_monitor, target_host, target_port)