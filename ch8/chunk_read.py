poem = ''
readfile = open('relativity', 'rt')
chunk = 100

while True:
    fragment = readfile.read(chunk) # read() 함수는 파일의 끝까지 다 읽을 경우 '' 빈 문자열을 반환
    if not fragment: # 더이상 읽은 내용이 없으면(read 함수의 반환 값이 빈 문자열) break --> 빈 문자열은 False
        break
    poem += fragment

readfile.close()
print(len(poem))