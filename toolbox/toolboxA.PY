import socket

def send_audio_file(host, port, audio_file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to Toolbox B")
        try:
            with open(audio_file_path, 'rb') as audio_file:
                audio_binary = audio_file.read()
                s.sendall(audio_binary)
            print("Audio file sent to Toolbox B")
        except FileNotFoundError:
            print(f"File '{audio_file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    host = 'localhost'  # Change to the IP of Toolbox B
    port = 12345  # Choose a port for communication
    audio_file_path = 'D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\recorded audio\\beast.wav'  # Replace with the path to your audio file
    send_audio_file(host, port, audio_file_path)
