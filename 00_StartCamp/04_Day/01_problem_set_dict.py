"""
python dictionary 문제
"""

# #1. 평균을 구하세요
# score = {
#     '수학' : 80,
#     '국어' : 90,
#     '음악' : 100
# }

# a = 0

# for value in score.values():
#     a += value
# print(a/len(score))

# # 2. 반 평균을 구하세요. -> 전체 평균
# score = {
#     'a' :{
#         '수학' : 80,
#         '국어' : 90,
#         '음악' : 100
#     } ,
#     'b' :{
#         '수학' : 80,
#         '국어' : 90,
#         '음악' : 100
#     } 
# }

# a_sc = 0
# b_sc = 0
# total = 0
# leng = 0
# for value in score.values():
#     for value in score['a'].values():
#         a_sc += value
#     print(f'A반 점수 : {a_sc/leng}') 
#     for value in score['b'].values():
#         b_sc += value
#     print(f'B반 점수 : {b_sc/leng}') 
#     leng += 1
# total = a_sc + b_sc
# print(f'총 평균은 : {total/leng}')

# for person_score in scores.values():
#     for subject_score in person_socores.values():

#average_score = total_score / length

#도시별 최근 3일 온도입니다.

city = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -2, 10],
    '부산' : [2, -2, 9]
}

#3-1. 도시별 최근 3일의 온도 평균은?
#3-2. 도시 중 최근 3일 중에 가장 추웠던, 가장 더웠던 곳은?
#3-3. 서울은 영상 2도였던 적이 있나요? -> EX. 있다. 없다.


# 1.
for name, temp in city.items():
    average_temp = sum(temp) / len(temp)
    print('{} : {:.2f}' .format(name, average_temp))
        
#2.
for name, temp in city.items():
    cold_temp = 

#3.
print(2 in city['서울'])