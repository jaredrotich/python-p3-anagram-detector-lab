# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [word for word in word_list if sorted(word.lower()) == sorted(self.word) and word.lower() != self.word]
