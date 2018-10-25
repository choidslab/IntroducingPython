poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

# with문을 통해 파일을 자동으로 닫을 수 있다.
# Python에서는 이를 context manager라고 한다.
# context manager 코드 한 줄이 실행된 후 자동으로 파일을 닫아준다.(잘 실행되거나, 예외 발생)
with open('relativity', 'wt') as fout:
    fout.write(poem)