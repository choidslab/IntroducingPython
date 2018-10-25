from collections import namedtuple

Bird = namedtuple('Bird', 'bill tail')
duck = Bird('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

#parts 딕셔너리에서 key, value 값을 각각 추출하여 Duck클래스에 인자로 전달
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Bird(**parts)
print(duck2)