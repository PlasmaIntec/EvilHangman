class Strategy:
    def choose_char(self) -> str:
        pass

class MostFrequentStrategy(Strategy):
    def __init__(self):
        self.char_by_freq = "ETAONRISHDLFCMUGYPWBVKJXZQ"
        self.i = 0

    def choose_char(self) -> str:
        char = self.char_by_freq[self.i].lower()
        self.i += 1
        return char