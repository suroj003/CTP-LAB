class Frequency:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        words = self.text.lower().split()
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        print("Word Frequency:")
        for word in freq:
            print(word, ":", freq[word])

    def char_count(self):
        freq = {}

        for ch in self.text.lower():
            if ch == " ":
                continue

            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        print("\nCharacter Frequency:")
        for ch in freq:
            print(ch, ":", freq[ch])


text = input("Enter a text: ")

obj = Frequency(text)

obj.word_count()
obj.char_count()