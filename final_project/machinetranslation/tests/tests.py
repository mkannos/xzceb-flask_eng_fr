import unittest
from translator import englishToFrench, frenchToEnglish

class TranslationTestCase(unittest.TestCase):
    def englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')

    def frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish("None"), '')

if __name__ == '__main__':
    unittest.main()