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
        emotion = "Neutral 😐"
    
    emotion_replies = {
        "Happy 😊": "That's wonderful to hear!",
        "Sad 😢": "I'm here for you.",
        "Angry 😠": "Take a deep breath, it'll be okay.",
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
        "emotion": emotion,
        "reply": reply,
    }
