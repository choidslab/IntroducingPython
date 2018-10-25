poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

if __name__ == "__main__":
    # 파일에 쓸 문자열이 클 경우 chunk 단위로 나누어서 파일에 쓸 수 있음
    fout = open('relativity3', 'wt')

    size = len(poem)
    offset = 0
    chunk = 100

    while True:
        if offset > size:
            break
        fout.write(poem[offset:offset+chunk])
        offset += chunk

    # file close
    fout.close()