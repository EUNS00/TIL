word = ('2+3*4/5')
test = []
result = []

for tc in word:
    if tc == '+' or tc == '-' or tc == '*' or tc == '/':
        test.append(tc)
    else:
        result.append(tc)

while test != []:
    t = test.pop()
    result.append(t)

result = ''.join(result)
print(result)
