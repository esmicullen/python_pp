# #문자열
# for ch in "뇨롱" :
#     print(ch,end=' ')
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #list
# for item in ["힙합","발라드"] :
#     print(item)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #튜플
# for item in (2929,39393):
#     print(item)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #set
# for item in {"wsm","java","python"}:
#     print(item)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #딕셔너리
# pl = {"C":1972,"JAVA":1995,"Python":1991}
# for item in pl:
#     print(item)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# for key in pl.keys():
#     print(key)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# for val in pl.values():
#     print(val)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# for key,val in pl.items():
#     print(key,val)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# num_list = [-5,127,-13,9,-21,100]
# for a in num_list:
#     if (0<a): print(a)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# num_list = [13,8,7,55,100,2,12,10,17]
# for b in num_list:
#     if (b%2==0): print(b)
#     else: print("홀수이다")
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# hj = ["짝","홀"]
# for num in num_list:
#     [print(hj[num%2])]
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #자리수
# for num in num_list:
#     print('{}은 {}자리수이다'.format(num,len(str(num))))
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

svt = {"S.CUPS":90,"JUNGHAN":100,"JOSHUA":95,
       "JUN":50,"HOSHI":85,"WONWOO":80,"WOOZI":75,
       "THE8":30,"MINGYU":45,"DK":65,
       "SEUNGKWAN":85,"VERNON":30,"DINO":25}

for name,j in svt.items():
    if j>=60: print(f'{name}은 {j}점으로 합격입니다')
    else: print(f'{name}은 {j}점으로 불합격입니다')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#range함수
#range(시작,종료,증가)
#range(기본값0,종료값,기본값10
print(list(range(0,10,1)))
print(list(range(10,0,-1))) #단계값이 음수면 역순
print(list(range(0,10,5)))

print(list(range(0,10)))
print(list(range(10)))

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#리스트
NCTdream = ['런쥔','제노','해찬','마크','재민','지성','천러']
for i in range(0,len(NCTdream)):
    print(i+1,NCTdream[i])

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

for i,member in enumerate(NCTdream):
    print(i+1,member)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

plus = 0
for su in range(1,201,1):
    if(su%3==0):plus = plus+su
print(plus)

plus = 0
for su in range(500,1001,1):
    if(su%5==0):plus = plus+su
print(plus)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#sum()함수,max,min
l = [1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

for i in range(1,10,1):
    for j in range(1, 10, 1):
        print(f'{i}x{j}={j * i}')

