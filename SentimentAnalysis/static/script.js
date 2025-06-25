function analyzeText() {
  const text = document.getElementById("inputText").value;
  if (!text) return alert("Please enter some text!");

  fetch('/SentimentAnalysis', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text })
  })
  .then(response => response.json())
  .then(data => {
    const output = `
      <strong>🧾 Tokens:</strong> ${data.tokens.join(", ")}<br>
      <strong>📚 Lemmas:</strong> ${data.lemmas.join(", ")}<br>
      <strong>🔠 POS Tags:</strong> ${JSON.stringify(data.pos_tags)}<br>
      <strong>🏷️ Named Entities:</strong> ${JSON.stringify(data.entities)}<br>
      <strong>📐 Dependencies:</strong> ${JSON.stringify(data.dependencies)}<br>
      <strong>📊 Sentiment Polarity:</strong> ${data.polarity}<br>
      <strong>🧠 Subjectivity:</strong> ${data.subjectivity}<br>
      <strong>💬 Detected Emotion:</strong> <span style="color:yellow">${data.emotion}</span><br>
      <strong>🤖 Smart Reply:</strong> <span style="color:#00ffcc">${data.reply}</span>
    `;
    document.getElementById("output").innerHTML = output;
  });
}

function startListening() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.onresult = function(event) {
    const text = event.results[0][0].transcript;
    document.getElementById("inputText").value = text;
    analyzeText();
  };
  recognition.start();
}
