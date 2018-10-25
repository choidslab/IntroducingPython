class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name)

if __name__ == "__main__":
    fowl = Duck("Howard")
    print(fowl.name)
    print(fowl.get_name())

    fowl.name = "Tim"
    print(fowl.name)