def calc(equation):
    result = 0
    c = '0'
    equation = c + equation
    a = equation.replace("-","+-")
    b = a.split("+")
    for i in b:
        result += int(i)
    return result

print(calc('123+2-124')) 
print(calc('-12+12-7979+9191')) 
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
