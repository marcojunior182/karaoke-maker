import speech_recognition as sr
import whisper
from langdetect import detect

# Function to create and open a txt file
def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)

class Transcription:
    def __init__(self):
        # Inicialize o reconhecedor
        self.recognizer = sr.Recognizer()

    def transcrever_audio(self, audio_file):
        # Carrega o arquivo de áudio
        model = whisper.load_model("base")
        result = model.transcribe(audio_file)
        transcribed_text = result["text"]
        print(transcribed_text)

        # Detect the language
        language = detect(transcribed_text)
        print(f"Detected language: {language}")

        # Create and open a txt file with the text
        create_and_open_txt(transcribed_text, f"output_{language}.txt")

        return transcribed_text

# Exemplo de uso
#transcription = Transcription()
#texto_transcrito = transcription.transcrever_audio("KaraokeAudios/Home.mp3")
