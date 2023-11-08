import socket
import sounddevice as sd
import soundfile as sf
import io  # Add this import statementdd

def receive_and_process_audio(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        print("Connected to Toolbox A")
        try:
            while True:
                audio_binary = conn.recv(65536)  # Adjust the buffer size as needed
                audio_file = io.BytesIO(audio_binary)
                audio_data, sample_rate = sf.read(audio_file, dtype='float32')
                process_audio(audio_data, sample_rate)  # Implement your audio processing here
        except KeyboardInterrupt:
            pass

def process_audio(audio_data, sample_rate):
    # Implement audio processing using your toolbox models (encoder, synthesizer, and vocoder)
    # After processing, you can choose to play or save the audio data
    print("Hello")

if __name__ == "__main__":
    host = 'localhost'  # Change to the IP of Toolbox A
    port = 12345  # Use the same port as in Toolbox A
    receive_and_process_audio(host, port)
