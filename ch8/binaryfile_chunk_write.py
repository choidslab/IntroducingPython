bdata = bytes(range(0, 256))
fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk]) # 텍스트와 동일하게 chunk 단위로 쓰기 가능
    offset += chunk

fout.close()