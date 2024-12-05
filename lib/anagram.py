# your code goes here!
class Anagram:
    def __init__(self, word):
        """
        Initializes the Anagram instance with a word.
        The word is stored in lowercase to make comparisons case-insensitive.
        """
        self.word = word.lower()

    def match(self, possible_anagrams):
        """
        Takes a list of possible anagrams and returns the list of words 
        that are anagrams of the initialized word.
        """
        # Sort the letters of the original word for comparison
        sorted_word = sorted(self.word)
        # Filter and return words that are anagrams
        return [word for word in possible_anagrams if sorted(word.lower()) == sorted_word]
