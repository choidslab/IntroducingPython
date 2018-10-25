class Duck():
    def __init__(self, input_name):
        # double underscore
        self.__name = input_name

    @property
    def name(self):
        print("inside getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("inside setter")
        self.__name = input_name

if __name__ == "__main__":
    dk = Duck("DS")

    print(dk.name)
    print(dk.__name)