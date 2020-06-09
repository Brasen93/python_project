class Enigma:

    def __init__(self, sentence: str):
        self.sentence = sentence

    def encryptor(self):
        encrypted_sentence = ""
        old_letters = ['a', 'e', 'i', 'o', 'y']
        new_letters = ['y', 'i', 'o', 'a', 'e']

        for char in self.sentence:
            if char.lower() in old_letters:
                index_of_char = old_letters.index(char.lower())
                if char.isupper():
                    encrypted_sentence += new_letters[index_of_char].upper()
                else:
                    encrypted_sentence += new_letters[index_of_char]
            else:
                encrypted_sentence += char

        return encrypted_sentence

    def decryptor(self):
        decrypted_sentence = ""
        old_letters = ['y', 'i', 'o', 'a', 'e']
        new_letters = ['a', 'e', 'i', 'o', 'y']

        for char in self.sentence:
            if char.lower() in old_letters:
                index_of_char = old_letters.index(char.lower())
                if char.isupper():
                    decrypted_sentence += new_letters[index_of_char].upper()
                else:
                    decrypted_sentence += new_letters[index_of_char]
            else:
                decrypted_sentence += char

        return decrypted_sentence
