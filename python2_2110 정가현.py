# 2110 정가현

# 1
def sum_odd(ph_num):
    sum_re = 0
    for i in range(0, len(ph_num)):
        if (int)(ph_num[i]) % 2 != 0:
            sum_re = sum_re + (int)(ph_num[i])
    return sum_re


result = sum_odd('01012345678')
print(result)
result = sum_odd('01022224444')
print(result)
result = sum_odd('01099999999')
print(result)


# 2
def encrypt(moon):
    mun = moon.replace('a', '*')
    mun = mun.replace('e', '*')
    mun = mun.replace('i', '*')
    mun = mun.replace('o', '*')
    mun = mun.replace('u', '*')
    mun = mun.replace('A', '*')
    mun = mun.replace('E', '*')
    mun = mun.replace('I', '*')
    mun = mun.replace('O', '*')
    mun = mun.replace('U', '*')
    return mun


print(encrypt('ive'))
print(encrypt('nct dream'))
print(encrypt('AEiou'))
print(encrypt('GOOGLE'))
print(encrypt('BTS'))


# 3
def dec_to_bin(su):
    return bin(su)


print(dec_to_bin(10))


# 4

# 5
def fare_pc(minute):
    if minute < 10:
        r = 1000
    elif minute % 10 > 0:
        r = ((minute // 10) + 1) * 1000
    else:
        r = minute // 10 * 1000
    return r


print(fare_pc(minute=3))
print(fare_pc(minute=20))
print(fare_pc(minute=34))


# 6
def get_bmi(height, weight):
    ki = height / 100
    rt = weight / (ki * ki)
    bmi = ''
    if rt < 18.5:
        bmi = '저체중'
    elif 18.5 <= rt < 23:
        bmi = '정상'
    elif 23 <= rt < 25:
        bmi = '과체중'
    elif 25 <= rt:
        bmi = '비만'

    return bmi, round(rt, 2)


print(get_bmi(height=170, weight=60))
print(get_bmi(height=150, weight=60))
print(get_bmi(height=180, weight=50))
print(get_bmi(height=160, weight=60))


# 7
def minus_time(hour1, minute1, hour2, minute2):
    h = hour1 - hour2
    m = minute1 - minute2
    boo = ''

    if h < 0:
        boo = '-'
    elif m < 0:
        boo = '-'
    else:
        boo = '+'

    return boo, h, m  # 절댓값 함수 이름이 뭐더라


sign, hour, minute = minus_time(hour1=13, minute1=40, hour2=6, minute2=33)
print(sign, hour, minute)
sign, hour, minute = minus_time(hour1=6, minute1=33, hour2=13, minute2=40)
print(sign, hour, minute)


# 8
def rgb_to_hex(r, g, b):
    r1 = ''
    g1 = ''
    b2 = ''
    return
# 2110 정가현
