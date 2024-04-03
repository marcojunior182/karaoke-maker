import speech_recognition as sr


class Transcription:
    def __init__(self):
        # Inicialize o reconhecedor
        self.recognizer = sr.Recognizer()

    def transcrever_audio(self, audio_file):
        # Carrega o arquivo de áudio
        audio = sr.AudioFile(audio_file)
        with audio as source:
            audio = r.record(source)

        try:
            # Usa o reconhecedor para transcrever o áudio
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            # Caso o áudio não seja reconhecido
            return "Não foi possível entender o áudio"
        except sr.RequestError as e:
            # Caso ocorra um erro na requisição ao serviço de reconhecimento
            return f"Erro na requisição ao serviço de reconhecimento: {e}"

# Exemplo de uso
transcription = Transcription()
texto_transcrito = transcription.transcrever_audio("../KaraokeAudios/Home.wav")
print(texto_transcrito)
