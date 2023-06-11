from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator()

def englishToFrench(englishText):
    try:
        frenchText = translator.translate(englishText, "en", "fr")
        return frenchText
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def frenchToEnglish(frenchText):
    try:
        englishText = translator.translate(frenchText, "fr", "en")
        return englishText
    except Exception as e:
        print(f"Translation error: {e}")
        return None