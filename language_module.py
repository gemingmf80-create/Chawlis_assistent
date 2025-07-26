from googletrans import Translator

translator = Translator()

def translate_input(text, target_lang="en"):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text

def translate_output(text, user_lang="en"):
    try:
        return translator.translate(text, dest=user_lang).text
    except:
        return text