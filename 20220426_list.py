empty_list = []
player = ['Faker', 10, True]
print(len(empty_list))
print(len(player))
print(type(empty_list), type(player))
empty_list2 = list()
print(len(empty_list2))
message = list('miracle')
print(message)
#numbers = list(56)
#print(numbers)
print(player)
player = player + [10, 11]
print(player)
player.append([20,21])
print(player)
player.append(56)
print(player)
player.insert(2, 'SKT T1')
print(player)
player.extend([30,31])
print(player)
#apende() : 리스트 통쨰로 추가
#+= , extend() : 리스트 풀어서 하나씩 추가
print(player)
player.append(40)
print(player)
#맨끝에 50추가 insert()
#player.insert(11, 50) or
player.insert(len(player), 50)
print(player)
#수정
print(player[0])
player[0] = 'Stitch'
print(player[0])
print(player)
print(player[6])
player[6] = 16
print(player[6])
print(player)
#삭제
del player[2]
print(player)
player.remove(30)
print(player)
player.pop()
print(player)
player.pop(2)
print(player)
# player.clear()
# print(player)
#remove() : 값으로 지우기
#pop(index), del 리스트명[index]: 인덱스로 지우기
#pop() : 맨 뒤에서 지우기
print(100 in player)
print(10 in player)
print('SEVENTEEN' in player)
print(player)
player[0] = 13
print(player)
player.sort()
print(player)
player.reverse()
print(player)
#*********************8
a = range(14)
print(a)
a2 = list(a)
print(a2)
print(list(range(14)))
b = range(1, 14+1)
print(list(b))
c = range(1, 14+1, 2)

