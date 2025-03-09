import whisper

# Load Whisper's "large" model for best translation accuracy
model = whisper.load_model("large")

# Path to your Swedish movie
video_path = r"C:\Users\akhil\Downloads\Bara sex 1 Vill du ha sex med mig SVT Play.mp4"


# Transcribe and translate
result = model.transcribe(video_path, task="translate")

# Save the translated text as a .srt subtitle file
with open("translated_subtitles.srt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment['start']
        end = segment['end']
        text = segment['text']

        # Format subtitles in SRT format
        f.write(f"{segment['id'] + 1}\n")
        f.write(f"{format_time(start)} --> {format_time(end)}\n")
        f.write(f"{text}\n\n")

# Helper function for formatting time in SRT format
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

print("✅ Translation complete! Check 'translated_subtitles.srt'")
