import unittest
import enigma


class TestEnigma(unittest.TestCase):
    """Tests for enigma.py"""

    def test_encryptor(self):
        """This test checks whether the encrypting works correctly"""
        sentence_01 = enigma.Enigma('tekst taki nowy')
        self.assertEqual(sentence_01.encryptor(), 'tikst tyko nawe')

    def test_decryptor(self):
        """This test checks whether the decrypting works correctly"""
        sentence_02 = enigma.Enigma('unowirsetit')
        self.assertEqual(sentence_02.decryptor(), 'uniwersytet')

    def test_upper_case_letter_encryptor(self):
        """This test checks whether the encrypting works with upper case letter"""
        sentence_03 = enigma.Enigma('OLBRZYM')
        self.assertEqual(sentence_03.encryptor(), 'albrzem')

    def test_upper_case_letter_decryptor(self):
        """This test checks whether the decrypting works with upper case letter"""
        sentence_04 = enigma.Enigma('ALYF')
        self.assertEqual(sentence_04.decryptor(), 'olaf')

    def test_spaces_encryptor(self):
        """This tests checks whether the encrypting works with spaces in sentence"""
        sentence_05 = enigma.Enigma('to jest zdanie ze spacją')
        self.assertEqual(sentence_05.encryptor(), 'ta jist zdynoi zi spycją')

    def test_spaces_decryptor(self):
        """This tests checks whether the decrypting works with spaces in sentence"""
        sentence_06 = enigma.Enigma('ymydiusz mazyrt')
        self.assertEqual(sentence_06.decryptor(), 'amadeusz mozart')

    def test_encryptor_does_nothing(self):
        """This tests checks whether the encryptor does not encrypt if there is nothing to encrypt"""
        sentence_07 = enigma.Enigma('szczur')
        self.assertEqual(sentence_07.encryptor(), 'szczur')

    def test_decryptor_does_nothing(self):
        """This tests checks whether the decryptor does not decrypt if there is nothing to decrypt"""
        sentence_08 = enigma.Enigma('brzuch')
        self.assertEqual(sentence_08.decryptor(), 'brzuch')


if __name__ == '__main__':
    unittest.main()
