year_lists = [1980]

for i in range(5):
    year_lists.append(year_lists[i] + 1)

print(year_lists)
print(year_lists[3])
print(year_lists[-1])

things = ["mozzarella", "cinderella", "salmonella"]

for thing in things:
    print(thing.capitalize()) # capitalize() 함수는 문자열의 첫 글자를 대문자로 변경

print(things)

things[0] = things[0].upper()
print(things)

del(things[-1])
print(things)

surprise = ["Groucho", "Chico", "Harpo"]

surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise[-1])

e2f ={'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

print(e2f['walrus'])

f2e = dict()
for k, v in e2f.items():
    f2e[v] = k

print(f2e)
print(f2e['chien'])

print(e2f.keys())

life = {'animals': {
        'cats': 'henri',
        'octopi': 'Grumpy',
        'emus': 'Lucy'
        },
        'plants': {},
        'other': {}
    }
print(life)

print("***life keys***")
for key in life.keys():
    print(key)

print('***animals keys***')
for animals_key in life['animals'].keys():
    print(animals_key)

print('***animals-cats values***')
print(life['animals']['cats'])