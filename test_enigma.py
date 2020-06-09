import unittest
import enigma


class TestEnigma(unittest.TestCase):
    """Tests for enigma.py"""

    def setUp(self) -> None:
        self.encryptor = enigma.Enigma(['a', 'e', 'i', 'o', 'y'], ['y', 'i', 'o', 'a', 'e'])
        self.decryptor = enigma.Enigma(['y', 'i', 'o', 'a', 'e'], ['a', 'e', 'i', 'o', 'y'])

    def test_encryptor(self):
        """This test checks whether the encrypting works correctly"""
        sentence_01 = 'tekst taki nowy'
        self.assertEqual(self.encryptor.enigmator(sentence_01), 'tikst tyko nawe')

    def test_decryptor(self):
        """This test checks whether the decrypting works correctly"""
        sentence_02 = 'unowirsetit'
        self.assertEqual(self.decryptor.enigmator(sentence_02), 'uniwersytet')

    def test_upper_case_letter_encryptor(self):
        """This test checks whether the encrypting works with upper case letter"""
        sentence_03 = 'OLBRZYM'
        self.assertEqual(self.encryptor.enigmator(sentence_03), 'ALBRZEM')

    def test_upper_case_letter_decryptor(self):
        """This test checks whether the decrypting works with upper case letter"""
        sentence_04 = 'ALYF'
        self.assertEqual(self.decryptor.enigmator(sentence_04), 'OLAF')

    def test_spaces_encryptor(self):
        """This tests checks whether the encrypting works with spaces in sentence"""
        sentence_05 = 'to jest zdanie ze spacją'
        self.assertEqual(self.encryptor.enigmator(sentence_05), 'ta jist zdynoi zi spycją')

    def test_spaces_decryptor(self):
        """This tests checks whether the decrypting works with spaces in sentence"""
        sentence_06 = 'ymydiusz mazyrt'
        self.assertEqual(self.decryptor.enigmator(sentence_06), 'amadeusz mozart')

    def test_encryptor_does_nothing(self):
        """This tests checks whether the encryptor does not encrypt if there is nothing to encrypt"""
        sentence_07 = 'szczur'
        self.assertEqual(self.encryptor.enigmator(sentence_07), 'szczur')

    def test_decryptor_does_nothing(self):
        """This tests checks whether the decryptor does not decrypt if there is nothing to decrypt"""
        sentence_08 = 'brzuch'
        self.assertEqual(self.decryptor.enigmator(sentence_08), 'brzuch')


if __name__ == '__main__':
    unittest.main()
