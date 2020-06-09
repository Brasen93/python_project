class Enigma:

    def __init__(self, old_letters, new_letters):
        self.old_letters = old_letters
        self.new_letters = new_letters

    def enigmator(self, sentence):
        ready_sentence = ""
        # old_letters = ['a', 'e', 'i', 'o', 'y']
        # new_letters = ['y', 'i', 'o', 'a', 'e']

        for char in sentence:
            if char.lower() in self.old_letters:
                index_of_char = self.old_letters.index(char.lower())
                if char.isupper():
                    ready_sentence += self.new_letters[index_of_char].upper()
                else:
                    ready_sentence += self.new_letters[index_of_char]
            else:
                ready_sentence += char

        return ready_sentence
