poem = ''
readfile = open('relativity', 'rt')
while True:
    line = readfile.readline() # readline() 함수는 파일을 한 라인씩 읽어 들인다.
    if not line: # 파일의 끝에 도달했을 경우 while문 종료
        break
    poem += line

readfile.close()
print(len(poem))