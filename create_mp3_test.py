from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

from moviepy.editor import TextClip

from datetime import datetime

# # Função para converter tempo no formato 'HH:MM:SS,mmm' para segundos
# def time_to_seconds(time_str):
#     return sum(x * float(t) for x, t in zip([3600, 60, 1, 1/1000], time_str.replace(',', '.').split(':')))


# # import subprocess
# # import json

# # video_path = 'KaraokeVideos/Home.mp4'

# # def get_video_info(video_path):
# #     cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams', video_path]
# #     output = subprocess.check_output(cmd)
# #     info = json.loads(output)
# #     return info

# # info = get_video_info(video_path)
# # for stream in info['streams']:
# #     if stream['codec_type'] == 'video':
# #         fps = eval(stream['avg_frame_rate'])
# #         print(f"FPS do vídeo: {fps}")

# # get_video_info(video_path)



# # Caminho para o vídeo e para o arquivo de legenda
# video_path = 'KaraokeVideos/Home.mp4'
# subtitle_path = 'SrtFiles/Home.srt'

# # Carregar o vídeo
# video = VideoFileClip(video_path)

# # Gerar um clipe de texto para cada legenda
# subtitles = []
# with open(subtitle_path, 'r', encoding='utf-8') as file:
#     for line in file:
#         if '-->' in line:
#             start, end = line.split(' --> ')
#             start_seconds = time_to_seconds(start)
#             end_seconds = time_to_seconds(end)
#             duration = end_seconds - start_seconds
#             text = next(file).strip()
#             subtitle = TextClip(text, font='Arial', fontsize=24, color='yellow')
#             subtitle = subtitle.set_start(start_seconds).set_duration(duration).set_position(('center', 'bottom'))
#             subtitles.append(subtitle)

# # Combinar o vídeo com as legendas
# final_video = CompositeVideoClip([video] + subtitles)

# # Salvar o vídeo com as legendas embutidas
# final_video.write_videofile('video_com_legenda.mp4', codec='libx264')




def replace_audio(video_path, audio_path, output_path):
    """
    Substitui o áudio de um vídeo MP4 por um áudio MP3.

    Parâmetros:
        video_path (str): Caminho para o arquivo de vídeo MP4.
        audio_path (str): Caminho para o arquivo de áudio MP3.
        output_path (str): Caminho para salvar o vídeo resultante com o novo áudio.
    """
    # Carregar o vídeo e o áudio
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Substituir o áudio do vídeo pelo novo áudio
    video_with_new_audio = video.set_audio(audio)

    # Salvar o vídeo com o novo áudio
    video_with_new_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Exemplo de uso
replace_audio('video_com_legenda.mp4', 'KaraokeAudios/Home/accompaniment.wav', 'video_com_legenda_s_voz.mp4')
