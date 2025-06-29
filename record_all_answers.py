import sounddevice as sd
import wavio
import time

# List of questions (for prompt display only)
questions = [
    "1. आपका पूरा नाम क्या है?",
    "2. आपकी ईमेल आईडी और मोबाइल नंबर क्या है?",
    "3. आप किस शहर या स्थान में रहते हैं?",
    "4. आपने सबसे उच्च शिक्षा किस विषय में और किस यूनिवर्सिटी से की है?",
    "5. आपने उस डिग्री को किस महीने और वर्ष में पूरा किया था?",
    "6. आपने कितनी कंपनियों में काम किया है?",
    "7. पहली कंपनी का नाम क्या था और वहाँ आपका पद क्या था?",
    "8. आपने उस कंपनी में किस महीने और वर्ष से किस महीने और वर्ष तक काम किया?",
    "9. आपकी मुख्य जिम्मेदारियाँ क्या थीं?",
    "10. क्या आप वर्तमान में किसी कंपनी में कार्यरत हैं?",
    "11. वर्तमान कंपनी का नाम क्या है और आपने वहाँ कब से काम करना शुरू किया?",
    "12. आपकी वर्तमान जॉब प्रोफाइल और जिम्मेदारियाँ क्या हैं?",
    "13. आपकी प्रमुख स्किल्स क्या हैं?",
    "14. आप किस प्रकार की नौकरी की तलाश कर रहे हैं?"
]

DURATION = 15  # seconds per answer (adjust as needed)
FS = 44100     # Sample rate

print("🎤 ResumeKaruAI - Record All Answers\n")
print("Instructions: After you hear each question, speak your answer clearly.")
print(f"Each answer will be recorded for {DURATION} seconds.\n")

for idx, question in enumerate(questions, 1):
    input(f"Press Enter to start recording for Question {idx}: {question}\n")
    print(f"🔴 Recording... (Q{idx})")
    recording = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
    sd.wait()
    filename = f"answer_{idx}.wav"
    wavio.write(filename, recording, FS, sampwidth=2)
    print(f"✅ Saved as {filename}\n")
    time.sleep(1)

print("✅ All 14 answers recorded! Proceed to transcription.")
