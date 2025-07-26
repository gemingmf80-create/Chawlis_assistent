from voice_module import listen, speak
from emotion_module import update_emotion, get_emotion_response
from language_module import translate_input, translate_output
from memory_module import remember, recall

speak("Hello, I am Charlie, your AI assistant. How can I help you?")

while True:
    user_input = listen()
    if user_input in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        break

    update_emotion(user_input)
    translated = translate_input(user_input)
    memory = recall(translated)

    if memory:
        response = memory
    else:
        response = get_emotion_response(translated)
        remember(translated, response)

    final_output = translate_output(response)
    speak(final_output)