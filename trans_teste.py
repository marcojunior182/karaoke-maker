from datetime import timedelta
import os
import whisper

audio = 'KaraokeAudios/Home.mp3'

def transcribe_audio(path):
    model = whisper.load_model("base")  # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    srtFilename = os.path.join("SrtFiles", f"{os.path.basename(path).split('.')[0]}.srt")

    for segment in segments:
        startTime = "0" + str(timedelta(seconds=int(segment['start']))) + ',000'
        endTime = "0" + str(timedelta(seconds=int(segment['end']))) + ',000'
        text = segment['text']
        segmentId = segment['id'] + 1
        segment_text = f"{segmentId}\n{startTime} --> {endTime}\n{text.lstrip()}\n\n"

        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment_text)

    return srtFilename

transcribe_audio(audio)
