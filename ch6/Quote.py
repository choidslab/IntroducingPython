class Quote():

    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamanationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote("Elmer Fudd", "I'm hunting wabbits")
print(hunter.who(), 'says: ', hunter.says())

hunted1 = QuestionQuote("Bugs Bunny", "What's up, doc")
print(hunted1.who(), 'says: ', hunted1.says())

hunted2 = ExclamanationQuote("Daffy Duck", "It's rabbit season")
print(hunted2.who(), 'says: ', hunted2.says())