# Python에서는 파일I/O 수행 시 파일에서의 위치를 추적
# tell() 함수: 파일의 시작으로부터 현재 위치의 오프셋을 바이트 단위로 반환
# seek() 함수: 특정 바이트 오프셋으로 위치를 이동
readfile = open('bfile', 'rb')
print(readfile.tell())

# seek() 함수를 이용하여 파일의 끝에서 1byte 전 위치로 이동
print(readfile.seek(255))

bdata = readfile.read()
print(len(bdata))
print(bdata[0])

# seek() 함수: seek(offset, origin)
# origin 인자
#   - origin이 0일 때(default), 시작 위치에서 offset 바이트 이동
#   - origin이 1일 때, 현재 위치에서 offset 바이트 이동
#   - origin이 2일 때, 마지막 위치에서 offset 바이트 전 위치로 이동

# 다른 방법으로 마지막 바이트를 읽기

readfile2 = open('bfile', 'rb')
readfile2.seek(-1, 2) # 두 번째 origin 인자가 2이므로 마지막 위치에서 offset 바이트만큼 거꾸로 이동하므로 결국 파일의 끝에서 1바이트 전 위치로 이동

bdata = readfile2.read()
print(len(bdata))
print(bdata[0])