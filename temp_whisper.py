import whisper
import os
def asr():
    # Load the Whisper ASR model
    model = whisper.load_model("base")

    # Specify the path to the directory containing audio files
    audio_directory = "D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\recorded audio"

    # Output directory for saving text files
    output_directory = "D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\translate text"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all audio files in the specified directory
    audio_files = [os.path.join(audio_directory, filename) for filename in os.listdir(audio_directory) if filename.endswith(".flac") or filename.endswith(".wav")]

    for audio_file in audio_files:
        print(f"Processing audio file: {audio_file}")

        # Load and process the audio file
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # Detect the spoken language
        _, probs = model.detect_language(mel)
        detected_language = max(probs, key=probs.get)

        print(f"Detected language: {detected_language}")

        # Decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)

        # Print the recognized text
        recognized_text = result.text
        print(f"Recognized text: {recognized_text}")

        # Save the recognized text to a separate text file
        output_file_path = os.path.join(output_directory, os.path.splitext(os.path.basename(audio_file))[0] + ".txt")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(recognized_text)
            print(f"Saved recognized text to {output_file_path}")

        print(f"Deleted audio file: {audio_file}")