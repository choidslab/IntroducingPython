import csv

villains = [
    ['Doctor', 'No'],
    ['Ros', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]

if __name__ == "__main__":

    with open('villains', 'rt') as fin:
        csvin = csv.reader(fin)
        villains = [row for row in csvin]

    print(villains)