class Person():
    def __init__(self, name):
        self.name = name

# Person 클래스를 상속
class EmailPerson(Person):
    def __init__(self, name, email):
        # 상위 클래스 Person의 __init__함수를 이용하여 name 값을 초기화
        super().__init__(name)
        self.email = email

if __name__ == "__main__":
    p1 = EmailPerson("Kim", "Kim@kim.com")
    print(p1.name + ' & ' + p1.email)