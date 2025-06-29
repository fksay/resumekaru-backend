import os
import subprocess

NUM_QUESTIONS = 14

for i in range(1, NUM_QUESTIONS + 1):
    audio_file = f"answer_{i}.wav"
    transcript_file = f"transcript_{i}.txt"

    if not os.path.exists(audio_file):
        print(f"❌ {audio_file} not found, skipping.")
        continue

    print(f"🔍 Transcribing {audio_file}...")
    # This uses whisper from the command line (ensure openai-whisper is installed)
    result = subprocess.run(
        ["whisper", audio_file, "--language", "hi", "--model", "base", "--output_format", "txt"],
        capture_output=True, text=True
    )
    # Save only the main transcription to our file
    if os.path.exists(f"{audio_file[:-4]}.txt"):
        os.rename(f"{audio_file[:-4]}.txt", transcript_file)
        print(f"✅ Saved transcript to {transcript_file}")

print("🚦 All transcriptions complete. Please check your transcript files.")
