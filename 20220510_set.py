games = {'LOL', 'Destiny', 'Tetris', 1942, 2048}
empty = {}
empty_set = set()
print({'google': 'google.com', 18: 'naver.com'})
#요소 추가
games.add("테일즈러너")
games.update(("카트라이더", "지렁이"))
print(games)
#요소 제거
games.remove("LOL")
print(games)
#셋연산 교집합 합집합 차집합 대칭 차집합
#56p ~ 57p
#57p<<<<중요
a = set()
a.add('밥')
a.add('국')
print(a)
a.add('밥')
print(a)
idol = ['세븐틴', '스트레이키즈', '악뮤', '방탄소년단', '방탄소년단']
print(idol)
print(list(set(idol)))
