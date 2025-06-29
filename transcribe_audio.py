import whisper

# Load Whisper model (you can use "base" or "small" or "medium")
model = whisper.load_model("base")

# Transcribe the recorded audio
result = model.transcribe("answer_1.wav", language="hi")

# Save output to a text file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcription complete. Saved to transcription.txt")
