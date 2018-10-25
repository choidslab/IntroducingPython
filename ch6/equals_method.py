class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

if __name__ == "__main__":
    first = Word('ha')
    second = Word('HA')
    third = Word('eh')

    # equals() 호출
    print(first.equals(second))
    print(first.equals(third))
    print('\n')
    # __eq__() 호출
    print(first == second)
    print(first == third)