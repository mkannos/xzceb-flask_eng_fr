from deep_translator import MyMemoryTranslator

"""
Creates a Language Translator Service between French and English.
"""

def englishToFrench(englishText):
    translator = MyMemoryTranslator

    try:
        frenchText = translator.translate(englishText, "en", "fr")
        return frenchText
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator

    try:
        englishText = translator.translate(frenchText, "fr", "en")
        return englishText
    except Exception as e:
        print(f"Translation error: {e}")
        return None