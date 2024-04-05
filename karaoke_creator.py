from pytube import YouTube
from spleeter.separator import Separator
from transcription import Transcription
import os

path = 'KaraokeVideos/'
audiopath = 'KaraokeAudios/'

class KaraokeCreator:
    def __init__(self, youtube_url):
        self.youtube_url = youtube_url
        self.transcription = Transcription()   # Substitua por uma instância de Transcription quando implementada

    def download_video_audio(self):
        yt = YouTube(self.youtube_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(output_path=path)
        audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        audio_file_path = os.path.join(audiopath, audio.default_filename)
        audio.download(filename=audio_file_path)
        print(f'Download completed of {video.title}')
        self.title = video.title
        self.audio_file_path = audio_file_path

    def remove_vocals(self):
        print('Initializing vocal video removal')
        print(self.audio_file_path)
        if not os.path.exists(self.audio_file_path):
            raise ValueError("Audio not found. Please check the file path.")
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(self.audio_file_path, audiopath)
        print(f'Vocals removed and accompaniment saved in: {audiopath}')

    def criar_karaoke(self):
        self.download_video_audio()
        self.remove_vocals()
        # Aqui você pode adicionar a lógica para transcrição e sincronização de legendas
        # self.texto_transcrito = self.transcription.transcrever_audio(self.audio_file_path)

# Exemplo de uso
karaoke_creator = KaraokeCreator('https://www.youtube.com/watch?v=DHEOF_rcND8')
karaoke_creator.criar_karaoke()