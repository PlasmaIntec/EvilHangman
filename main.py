from collections import defaultdict

from strategy import MostFrequentStrategy

class Game:
    def __init__(self, dictionary = None, guesses = 26, size = 4) -> None:
        if not dictionary:
            self.dictionary = Game.get_scrabble_words()
        else:
            self.dictionary = dictionary
        self.dictionary = [e for e in self.dictionary if len(e) == size]
        self.guesses = guesses
        self.size = size
        self.pattern = "-" * size

    def guess(self, guess = None) -> None:
        if guess == None:
            char = input("guess a letter: ")
        else:
            char = guess

        if not char.isalpha():
            print("expected char")
            return
        if len(char) > 1:
            print("expected single char")
            return

        # select largest word class as remaining word set
        word_class = self.get_word_class(char)
        largest_word_class, pattern = max((word_class[k], k) for k in word_class)
        self.dictionary = set(largest_word_class)
        self.pattern = self.merge_pattern(pattern)

        # print("pattern: %s" % self.pattern)

        self.guesses -= 1

    def get_scrabble_words() -> set[str]:
        scrabble_words = set()

        scrabble_file = open("scrabble.txt", "r")
        for word in scrabble_file:
            scrabble_words.add(word.strip().lower())

        return scrabble_words

    def get_word_class(self, char) -> defaultdict:
        word_class = defaultdict(list)

        for word in self.dictionary:
            pattern = Game.get_pattern(word, char)
            word_class[pattern].append(word)

        return word_class

    def get_pattern(word, char) -> str:
        return "".join([c if c == char else "-" for c in word])

    def merge_pattern(self, pattern) -> str:
        return "".join([self.pattern[i] if self.pattern[i] != "-" else pattern[i] if pattern[i] != "-" else "-" for i in range(self.size)])

    def is_game_over(self) -> bool:
        return self.guesses == 0 or all(e != "-" for e in self.pattern)

    def play() -> int:
        game = Game(guesses=10)
        strategy = MostFrequentStrategy()
        
        game.guess(strategy.choose_char())

        while not game.is_game_over():
            game.guess(strategy.choose_char())

        if game.guesses > 0:
            print("win with: %s" % game.guesses)
        else:
            print("lose")

        return game.guesses

sample_dictionary = set(["love", "hope", "fear"])
Game.play()