class Car():
    def exclaim(self):
        print("I'm a Car")

class Yugo(Car):
    # 함수 오버라이드
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    # 하위 클래스에서 추가된 함수
    def need_a_push(selfs):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()
