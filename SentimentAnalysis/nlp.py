import spacy
from textblob import TextBlob

nlp_spacy = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp_spacy(text)
    blob = TextBlob(text)

    tokens = [token.text for token in doc]
    lemmas = [token.lemma_ for token in doc]
    pos_tags = [(token.text, token.pos_) for token in doc]
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)


    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negetive"
    else:
        sentiment = "Neutral"


    if "hate" in text.lower() or "angry" in text.lower() or "Nonscence" in text.lower() or "stupid" in text.lower():
        emotion = "Angry 😠"
    elif "disgust" in text.lower() or "eww" in text.lower():
        emotion = "Disgusted 🤢"
    elif "wow" in text.lower() or "surprise" in text.lower() or "ohh" in text.lower():
        emotion = "Surprised 😲"
    elif polarity > 0.3:
        emotion = "Happy 😊"
    elif polarity < -0.3:
        emotion = "Sad 😢"
    else:
        emotion = "Normal 😐"
    
    emotion_replies = {
        "Happy 😊": "That's wonderful to hear!",
        "Sad 😢": "I'm here for you.",
        "Angry 😠": "We understand your frustration and appreciate the input. Take a deep breath, and stay calm.",
        "Disgusted 🤢": "That's quite unpleasant!",
        "Surprised 😲": "Wow, that's unexpected!",
        "Neutral 😐": "Thanks for sharing your thoughts."
    }   

    reply = emotion_replies.get(emotion, "Thanks for sharing!")

    return {
        "tokens": tokens,
        "lemmas": lemmas,
        "pos_tags": pos_tags,
        "entities": ents,
        "dependencies": dependencies,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "Sentiment": sentiment,
        "emotion": emotion,
        "reply": reply,
    }
