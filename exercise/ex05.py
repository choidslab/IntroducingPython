# 5.1
# zoo.py 정의
from exercise import zoo
print(zoo.hours())

# 5.2 as를 이용한 import
from exercise import zoo as menagerie
print(menagerie.hours())

# 5.3 from 모듈이름 from 모듈함수 --> 모듈 이름 없이 함수 이름만으로 접근이 가능
from exercise.zoo import hours
print(hours())

# 5.4
from exercise.zoo import hours as info
print(info())

# 5.5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# 5.6
from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

# 5.7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
