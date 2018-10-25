class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property # getter
    def name(self):
        print("inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name

if __name__ == "__main__":
    fowl = Duck("Howard")
    print(fowl.name)

    # 아래와 같은 접근은 불가능
    # print(fowl.get_name())

    fowl.name = "Tim"
    print(fowl.name)