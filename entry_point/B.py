import A

print('top-level B.py')
A.func()

if __name__ == '__main__':
    print('B.py 직접 실행')
else:
    print('B.py import되어 실행')