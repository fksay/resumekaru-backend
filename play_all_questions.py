
import time
import os
from gtts import gTTS

questions = [
    "आपका पूरा नाम क्या है?",
    "आपकी ईमेल आईडी और मोबाइल नंबर क्या है?",
    "आप किस शहर या स्थान में रहते हैं?",
    "आपने सबसे उच्च शिक्षा किस विषय में और किस यूनिवर्सिटी से की है?",
    "आपने उस डिग्री को किस महीने और वर्ष में पूरा किया था?",
    "आपने कितनी कंपनियों में काम किया है?",
    "पहली कंपनी का नाम क्या था और वहाँ आपका पद क्या था?",
    "आपने उस कंपनी में किस महीने और वर्ष से किस महीने और वर्ष तक काम किया?",
    "आपकी मुख्य जिम्मेदारियाँ क्या थीं?",
    "क्या आप वर्तमान में किसी कंपनी में कार्यरत हैं?",
    "वर्तमान कंपनी का नाम क्या है और आपने वहाँ कब से काम करना शुरू किया?",
    "आपकी वर्तमान जॉब प्रोफाइल और जिम्मेदारियाँ क्या हैं?",
    "आपकी प्रमुख स्किल्स क्या हैं?",
    "आप किस प्रकार की नौकरी की तलाश कर रहे हैं?"
]

os.makedirs("questions", exist_ok=True)

for i, q in enumerate(questions, 1):
    filename = f"questions/question_{i}.mp3"
    if not os.path.exists(filename):
        tts = gTTS(text=q, lang='hi')
        tts.save(filename)
    os.system(f'start questions/question_{i}.mp3')  # For Windows
    print(f"🔊 Playing Question {i}: {q}")
    time.sleep(6)  # Enough time for each question to be heard
