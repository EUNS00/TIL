from decouple import config
import requests
import csv

with open('movie.csv', newline='', encoding='utf-8')as f:
    reader = csv.DictReader(f)
    peopleNm = []
    #한줄씩 읽는다.
    for row in reader:
        print(row['peopleNm'])
        peopleNm.append(row['peopleNm'])
        print(peopleNm)






# print(movie.get('boxOfficeResult').get('weeklyBoxOfficeList')[num].get('movieNm'))
    movie_data=dict()
    with open('director.csv', 'w', newline='', encoding='utf-8')as f:
        #저장할데이터들의 필드 이름을 미리 지정
        fieldnames = ['peopleCd','peopleNm', 'repRoleNm', 'filmoNames']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank in peopleNm :
            key = config('API_KEY')
            res = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={0}&peopleNm={1}'.format(key, rank))
            movie = res.json()
            #필드이름을 CSV파일 최상단에 작성
            movie_data['peopleCd'] = movie.get('peopleListResult').get('peopleList')[0].get('peopleCd')
            movie_data['peopleNm'] = movie.get('peopleListResult').get('peopleList')[0].get('peopleNm')
            movie_data['repRoleNm'] = movie.get('peopleListResult').get('peopleList')[0].get('repRoleNm')
            movie_data['filmoNames'] = movie.get('peopleListResult').get('peopleList')[0].get('filmoNames')
            #dictionary를 순회하며 key에 해당하는 value를 한줄씩 작성한다
            writer.writerow(movie_data)