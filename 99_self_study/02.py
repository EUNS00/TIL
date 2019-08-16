from decouple import config
import requests
import csv

with open('boxoffice.csv', newline='', encoding='utf-8')as f:
    reader = csv.DictReader(f)
    movies = []
    for row in reader:
        print(row['movieCd'])
        movies.append(row['movieCd'])
        print(movies)
    movie_data=dict()
    with open('movie.csv', 'w', newline='', encoding='utf-8')as f:
        fieldnames = ['movieCd','movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm', 'peopleNm2']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank in movies :
            key = config('API_KEY')
            res = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={0}&movieCd={1}'.format(key, rank))
            movie = res.json()
            movie_data['movieCd'] = movie.get('movieInfoResult').get('movieInfo').get('movieCd')
            movie_data['movieNm'] = movie.get('movieInfoResult').get('movieInfo').get('movieNm')
            movie_data['movieNmEn'] = movie.get('movieInfoResult').get('movieInfo').get('movieNmEn')
            if movie.get('movieInfoResult').get('movieInfo').get('movieNmOg') == '' :
                movie_data['movieNmOg'] = '원문명 없음'
            else :
                movie_data['movieNmOg'] = movie.get('movieInfoResult').get('movieInfo').get('movieNmOg')
            if movie.get('movieInfoResult').get('movieInfo').get('audits') == [] :
                movie_data['watchGradeNm'] = '전체관람가'
            else :
                movie_data['watchGradeNm'] = movie.get('movieInfoResult').get('movieInfo').get('audits')[0].get('watchGradeNm')
            movie_data['openDt'] = movie.get('movieInfoResult').get('movieInfo').get('openDt')
            movie_data['showTm'] = movie.get('movieInfoResult').get('movieInfo').get('showTm')
            movie_data['genreNm'] = ''
            for i in movie.get('movieInfoResult').get('movieInfo').get('genres'):
                movie_data['genreNm'] += i.get('genreNm')
            if movie.get('movieInfoResult').get('movieInfo').get('directors') == [] :
                movie_data['watchGradeNm'] = '집계안함'
            else :
                movie_data['peopleNm'] = movie.get('movieInfoResult').get('movieInfo').get('directors')[0].get('peopleNm')
            movie_data['peopleNm2'] = ''
            if movie.get('movieInfoResult').get('movieInfo').get('actors') == [] :
                movie_data['watchGradeNm'] = '배우정보없음'
            else :
                for i in movie.get('movieInfoResult').get('movieInfo').get('actors'):
                    movie_data['peopleNm2'] += i.get('peopleNm')
            writer.writerow(movie_data)