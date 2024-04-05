from spleeter.separator import Separator
from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip
import os

texto_transcrito = 'output_en.txt'

class SyncSubtitles:
    def __init__(self):
        # Inicialização de variáveis e configurações
        self.separator = Separator('spleeter:2stems')
        self.font = 'Arial-Bold'
        self.fontsize = 24
        self.margin = 10

    def sincronizar_legendas(self, audio_file, texto_transcrito):
        # Extrai os vocais do áudio
        audio_path, _ = os.path.splitext(audio_file)
        vocals_file = f'{audio_path}_vocals.wav'
        self.separator.separate_to_file(audio_file, output_path=vocals_file)

        # Segmenta o áudio em frases
        # Utilize uma biblioteca de segmentação de frases, como o Vosk

        # Gera clipes de texto para cada frase
        texto_segmentado = ['Frase 1', 'Frase 2', '...']
        texto_clips = []
        for frase in texto_segmentado:
            texto_clip = TextClip(frase, font=self.font, fontsize=self.fontsize, color='white')
            texto_clips.append(texto_clip)

        # Sincroniza os clipes de texto com o áudio
        # Utilize um algoritmo de sincronização, como o Dynamic Time Warping (DTW)

        # Cria o vídeo final com as legendas
        audio_clip = AudioFileClip(vocals_file)
        video_clip = CompositeVideoClip([audio_clip], size=audio_clip.size)

        # Posiciona e insere os clipes de texto no vídeo
        for i, texto_clip in enumerate(texto_clips):
            start_time = i * 5  # Ajustar de acordo com a duração das frases
            end_time = start_time + texto_clip.duration
            texto_clip = texto_clip.set_position('bottom', margin=self.margin).set_duration(end_time - start_time)
            video_clip = video_clip.add_clip(texto_clip, start_time=start_time)

        # Salva o vídeo final
        video_clip.write_videofile(f'{audio_path}_legendado.mp4', fps=25)

        print('Legendas sincronizadas com sucesso!')

# Exemplo de uso
sync_subtitles = SyncSubtitles()
audio_file = '/path/to/audio.wav'
texto_transcrito = 'Texto transcrito do áudio...'
sync_subtitles.sincronizar_legendas(audio_file, texto_transcrito)
