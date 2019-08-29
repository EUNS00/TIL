word = input()

result = []

for i in word:
    if i == '(':
        result.append(i)
    elif i == ')':
        if result != []:
            result.pop()
        else:
            print(')이 더 많음.')
            break

if result != []:
    print('(이 {}개 남았습니다.'.format(len(result)))