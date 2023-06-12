"""
translator from eng to french
"""

from deep_translator import MyMemoryTranslator

# english to french
def english_to_french(english_text):
    """
    function to translate Englist to French
    """
    french_text = MyMemoryTranslator(source="en", target="fr").translate(english_text)
    print(french_text)

    return french_text

# french to english
def french_to_english(french_text):
    """
    function to translate French to English
    """
    english_text = MyMemoryTranslator(source="fr", target="en").translate(french_text)
    print(english_text)
    return english_text