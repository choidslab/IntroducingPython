readfile = open('relativity', 'rt')
lines = readfile.readlines() # 파일의 각 라인을 읽어들여 리스트의 각 요소로 저장
readfile.close()

print(len(lines)) # 라인 수 출력

for line in lines: # 각 라인이 저장된 리스트 lines의 항목을 하나씩 읽어서 출력하는 for문
    print(line, end="")

# 실행결과
# 5
# There was a young lady named Bright,
# Whose speed was far faster than light;
# She started one day
# In a relative way,
# And returned on the previous night.
