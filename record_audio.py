import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # Standard sample rate for Whisper
seconds = 5

print("🎤 Recording started. Speak now...")

recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')  # dtype fixed
sd.wait()

write("answer_1.wav", fs, recording)  # Proper WAV file
print("✅ Recording saved as answer_1.wav")
