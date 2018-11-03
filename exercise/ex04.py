# 4.1
guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4.2
start = 1

while True:
    if start == guess_me:
        print('found it!')
        break
    elif start < guess_me:
        print('too low')
    else:
        print('oops!')
        break
    start += 1

# 4.3
for i in [3, 2, 1, 0]:
    print(i)

# 4.4 list comprehension
number_list = [number for number in range(10) if number % 2 == 0]
print(number_list)

# 4.5 dict comprehension
squares = {i: i*i for i in range(10)}
print(squares)

# 4.6 set comprehension
setodd = {odd for odd in range(10) if odd % 2 == 1}
print(setodd)

# 4.7 tuple은 comprehension 없음, 대신 괄호를 이용하여 comprehension을 작성할 경우 generator 객체 생성
number_generator = ("Got %s" % number for number in range(10))
for item in number_generator:
    print(item)

# 4.8
def get_list():
    return ['Harry', 'Ron', 'Hermione']
print(get_list())

# 4.9 generator 함수는 generator comprehension 표현식이 너무 긴 경우 사용, return이 아닌 yield 문으로 제너레이터 객체 반환
def get_odds():
    for number in range(1, 10, 2):
        yield number

for count, number in enumerate(get_odds(), 1): # enumeratre()는 인덱스와 값을 함께 출력해야하는 경우 자주 사용된다.
    if count == 3:
        print(number)
        break

# 4.10
def test(func):
    def inner_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return inner_func()

@test
def greeting():
    print("Greetings, Earthling")

#print(greeting())

# 4.11
# Exception 클래스를 상속받아 OopsException 예외를 새롭게 정의
class OopsException(Exception):
    pass

try: # raise 문을 이용하여 강제로 예외를 발생
    raise OopsException
except OopsException:
    print('Caught a oops!')

# 4.12

