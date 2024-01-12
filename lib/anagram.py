# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        word_lower = self.word.lower()
        matches = []

        for anagram in possible_anagrams:
            anagram_lower = anagram.lower()

            if len(word_lower) != len(anagram_lower):
                continue

            if sorted(word_lower) == sorted(anagram_lower):
                matches.append(anagram)

        return matches