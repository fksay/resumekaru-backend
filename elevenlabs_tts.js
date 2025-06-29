async function playQuestion() {
    const text = document.getElementById("question").textContent;

    try {
        const response = await fetch("/speak", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error("TTS generation failed");
        }

        const blob = await response.blob();
        const audioUrl = URL.createObjectURL(blob);

        const audioPlayer = document.getElementById("audioPlayer");
        audioPlayer.src = audioUrl;
        audioPlayer.play();
    } catch (err) {
        alert("❌ Failed to fetch audio\n" + err.message);
        console.error(err);
    }
}
