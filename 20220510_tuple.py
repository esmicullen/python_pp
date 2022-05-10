t = ()
xy = (2560, 1440)
color = 129, 247, 216
print(t)
print(xy)
print(color)
print(xy + color)
print(xy * 2)
#패킹, 언패킹
color = 129, 247, 216 #패킹
red, green, blue = color #언패킹
print(red)
x, y = (1920, 1080)
print(y)
print(color[1]) #인덱싱
print(color[0:2]) #슬라이싱
#color[1] = 255 #타입 에러 : 'tuple' object does not support item assignment, 상수
new_tuple = xy+color+(1440, 1080)
print(new_tuple)
print(new_tuple.index(1440))
print(new_tuple.count(1440))
임채영, 이예진 = 10, 8
print(임채영)
print(이예진)
이예진, 임채영 = 임채영, 이예진
print(임채영)
print(이예진)
#temp = b
#b = a
#a = temp