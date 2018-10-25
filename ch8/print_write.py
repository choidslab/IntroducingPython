poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

if __name__ == "__main__":
    # file open
    fout = open('relativity2', 'wt')

    # print 함수를 이용한 파일 쓰기
    print(poem, file=fout)

    # file close
    fout.close()