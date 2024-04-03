from transcription import Transcription
from sync_subtitles import SyncSubtitles
from pytube import YouTube
from moviepy.editor import VideoFileClip
from spleeter.separator import Separator
import os
import logging

path = '../KaraokeVideos/'
audiopath = '../KaraokeAudios/'

#class KaraokeCreator:
#    def __init__(self, youtube_link):
#        self.youtube_url = youtube_url
#        self.transcription = Transcription()
#        self.sync_subtitles = SyncSubtitles()

#    def baixar_video(youtube_url, path):
        # Lógica para baixar o vídeo
#        yt = YouTube(youtube_url)
#        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#        video.download(output_path=path)
#        print(f'Download completed of {video.title}')
#        title = video.title
#        return title

def extrair_audio(title):
    # Cria um objeto VideoFileClip para o vídeo
    video_clip = VideoFileClip(os.path.join(path, title + '.mp4'))

    # Define o caminho do arquivo de áudio extraído
    audio_file = os.path.join(audiopath, title + '.mp3')

    # Extrai o áudio do vídeo e salva no caminho especificado
    video_clip.audio.write_audiofile(audio_file)

    print(f'Audio extracted and saved in: {audio_file}')
    return audio_file

def remover_vocais(audio_file):
    print('Initializing vocal video removal')
    # Verifica se o arquivo de áudio existe
    if not os.path.exists(audio_file):
        raise ValueError("Audio not found. Please check the file path.")

    # Cria uma instância do Separator com a configuração de 2 stems (vocais e acompanhamento)
    separator = Separator('spleeter:2stems')

    # Extrai os vocais e o acompanhamento do áudio e salva no caminho especificado
    logging.getLogger('spleeter').setLevel(logging.INFO)
    separator.separate_to_file(audio_file, audiopath)
    logging.getLogger('spleeter').setLevel(logging.INFO)

    print(f'Vocais removidos e acompanhamento salvo em: {audiopath}')

# Exemplo de uso
title = 'Home'
audio_file = extrair_audio(title)
remover_vocais(audio_file)

    #def criar_karaoke(self):
    #    self.baixar_video()
    #    self.extrair_audio()
    #    self.remover_vocais()
    #    texto_transcrito = self.transcription.transcrever_audio(self.audio_file)
    #    self.sync_subtitles.sincronizar_legendas(self.audio_file, texto_transcrito)
        # Lógica para criar o vídeo de karaokê
    #    pass
