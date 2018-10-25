poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

if __name__ == "__main__":
    # file open
    try:
        fout = open('relativity', 'xt') # xt 모드를 이용하여 기존의 파일을 덮어쓰지 않도록 하여 파일 보호
        fout.write('test test test')
    except FileExistsError: # 파일이 이미 존재할 경우 에러 발생
        print("relativity already exists!.")

    # file close
    fout.close()