from django.shortcuts import render
from datetime import datetime
import random
import requests

# 1. 기본 로직
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def img(request):
    return render(request, 'img.html')

# 2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

# 3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    context = {
        'name': name, 
        'age': age, 
        'pick': pick
        }
    return render(request, 'hello.html', context)

# 4. 실습
# 4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아.) 자기소개 페이지
def myself(request, name, age):
    context = {
        'name': name, 
        'age': age
        }
    return render(request, 'myself.html', context)
    
# 4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def mur(request, num1, num2):
    num3 = num1*num2
    context = {'num1': num1, 'num2': num2, 'num3': num3}
    return render(request, 'mur.html', context)

# 4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def Circle(request, r):
    result = r**2 *3.14
    context = {'r': r, 'result': result}
    return render(request, 'Circle.html', context)

#5 DTL(Django Template Language)
def template_language(request):
    menus = ['짜장', '짬뽕', '탕수육', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

# 6 실습
# 6-1. isbirth
def isbirth(request):
    today = datetime.now()
    if today.month == 10 and today.day == 22:
        result = True
    else:
        result = False
    context={
        'result': result,
    }
    return render(request, 'isbirth.html', context)


# 6-2 회문판별
def ispal(request, word):
    result = False
    if word==word[::-1]:
        result = True
        
    context={
        'result': result,
    }
    return render(request, 'ispal.html', context)

def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    my_lotto = random.sample(range(1, 46), 6)
    if real_lottos==sorted(my_lotto):
        result = '당첨'
    else:
        result = '꽝'
    context = {
        'real_lottos': real_lottos,
        'my_lotto': sorted(my_lotto),
        'result': result,
    }
    return render(request, 'lotto.html', context)

#7 form - get
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'catch.html', context)

#7-2
def ping(request):
    date = request.GET.get('date')
    context={
        'date': date,
    }
    return render(request, 'ping.html', context)

def pong(request):
    date = request.GET.get('date')
    context={
        'date': date,
    }
    return render(request, 'pong.html', context)

#8. form -get 실습
def art(request):
    return render(request, 'art.html')

def result(request):
    # 1. form으로 날린 데이터를 받는다.
    word = request.GET.get('word')
    # 2.ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3.fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')
    # 4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장
    font = random.choice(fonts)
    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context={
        'result': result,
    }
    return render(request, 'result.html', context)

#9. form - post
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context={
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'user_create.html', context)