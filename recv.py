import os
import socket
import uuid

def receive_file(save_directory, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Listening on {host}:{port}")
        conn, addr = s.accept()

        # Receive the original filename
        original_filename = str(uuid.uuid4()) + ".flac"
        
        # Build the full path for the received file
        save_path = os.path.join(save_directory, original_filename)

        # Ensure the save_directory exists
        os.makedirs(save_directory, exist_ok=True)

        with open(save_path, 'wb') as file:
            data = conn.recv(1024)
            while data:
                file.write(data)
                data = conn.recv(1024)
        print(f"File received and saved as {save_path}")

if __name__ == "__main__":
    save_directory = "D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\recv_translated audio"  # Replace with the directory where received files will be saved
    listen_host = "127.0.0.1"  # Listen on all available network interfaces
    listen_port = 12345  # Change to your desired port number

    while True:
        receive_file(save_directory, listen_host, listen_port)
