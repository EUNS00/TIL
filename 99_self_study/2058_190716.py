numbers = int(input())

a = numbers//1000
b = numbers//100
b_= b-a*10
c = numbers//10
c_= c-b*10
d = numbers
d_= d-c*10

print(f'{a+b_+c_+d_}')