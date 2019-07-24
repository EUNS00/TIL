def my_url(itemperpage = 10, **api):
    if 'key' not in api or 'targetDt' not in api:
        return '필수 요청 변수가 누락되었습니다.'
    
    if itemperpage not in range(1,11):
        return '1~10까지 값을 넣어주세요'
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemperpage={itemperpage}&'
    for key, value in api.items():
        base_url += f'{key}={value}&'
    return base_url