emotion_state = "neutral"

def update_emotion(text):
    global emotion_state
    if "thank" in text or "good" in text:
        emotion_state = "happy"
    elif "bad" in text or "stupid" in text:
        emotion_state = "sad"
    else:
        emotion_state = "neutral"

def get_emotion_response(text):
    if emotion_state == "happy":
        return f"I'm glad to hear that! You said: {text}"
    elif emotion_state == "sad":
        return f"That makes me feel sad. But I'm here for you. You said: {text}"
    else:
        return f"You said: {text}"