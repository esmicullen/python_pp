#예약어
import calendar
import keyword #import 가져오다 keyword 모듈
print(keyword.kwlist)

print('-'*20)

#달력보기
import calendar
print(calendar.month(2022,4))
print(calendar.month(2005,8))
print(calendar.month(1981,11))

print('-'*20)

#현재 날짜와 시간 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.day, now.month, now.year)
my_birthday = datetime.datetime(2005, 8, 15)
print(now-my_birthday)
christmas = datetime.datetime(2022,12,25)
print(christmas - now)

print('-'*20)
#윈도우 보기
#import tkinter as tk
#base = tk.Tk()
#base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
t.speed(1)
t.forward(300)
t.right(144)
t.forward(300)
t.right(144)
t.forward(300)
t.right(144)
t.forward(300)
t.right(144)
t.forward(300)
t.right(144)

t.mainloop()
