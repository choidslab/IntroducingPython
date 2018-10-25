class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

if __name__ == "__main__":
    c = Circle(5)
    print(c.radius)
    print(c.diameter)
