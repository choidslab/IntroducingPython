# 0~255 256 bytes 값 생성
bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
print(fout.write(bdata)) # write() 함수는 파일에 쓴 byte 수를 반환하기 때문에 bdata의 값을 정상적으로 쓴 경우 256이 출력된다.
fout.close()