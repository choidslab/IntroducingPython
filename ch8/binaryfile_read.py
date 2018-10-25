readfile = open('bfile', 'rb') # rb 모드로 열기
bdata = readfile.read()
print(len(bdata))
readfile.close()
