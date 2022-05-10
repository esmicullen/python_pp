#dictionary : 사전, 단어, 뜻 , key, value
d = {}
urls = {'google' : 'google.com', 18: 'unesco.org'}
print(d)
print(urls)
#요소 추가
urls['유튜브'] = 'youtube.com'
print(urls)
#요소 수정
urls['google'] = 'google.co.kr'
print(urls)
#요소 출력
print(urls['google'])
print(urls[18])
#요소 제거
del urls['유튜브']
print(urls)
#urls.pop()
urls.pop(18)
print(urls)
birthdays = {'다연' : 5, '자윤' : 11}
birthdays_list = [5, 11]
print(birthdays.get('다연'))
print('google.co.kr' in urls)
print('google in' in urls)
print(urls.values())
print(urls.keys())
print(urls.items())