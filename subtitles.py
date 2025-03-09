import whisper
import os

# Load Whisper's "large" model for best translation accuracy
model = whisper.load_model("small")


# Path to your movie
video_path = r"path"

# Transcribe and translate
deprecated_path = os.getenv("PATH", "")
os.environ["PATH"] = deprecated_path + os.pathsep + r"C:\path\to\your\ffmpeg\bin"

result = model.transcribe(video_path, task="translate")

# Format time function
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Save as .srt subtitle file
with open("translated_subtitles.srt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment['start']
        end = segment['end']
        text = segment['text']

        f.write(f"{segment['id'] + 1}\n")
        f.write(f"{format_time(start)} --> {format_time(end)}\n")
        f.write(f"{text}\n\n")

print("✅ Translation complete! Check 'translated_subtitles.srt'")
