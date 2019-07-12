# with open('writelines_ssafy.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())

# with open('writelines_ssafy.txt', 'w') as f:
#     for i in range(4):
#         f.write(f'{3-i}\n')  

#1. 각각의 라인을 리스트의 요소로 불러오기
with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

#2. 뒤집기
# sample = lines.reverse()
# sample = reversed(lines)
lines.reverse()

with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)