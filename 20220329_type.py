#숫자
student_number = 2110
age = 18
height = 167.3

#문자
name = '정가현'

print(f'학번 : {student_number} \n이름 : {name} \n나이 : {age} \n키 : {height}')

print(type(student_number))
print(type(name))
print(type(age))
print(type(height)) #float
print(type(10.27)) #float
print(type(10)) #int
print(type('1027')) #class str
print(10/27) #2.7
print(27/10) #몫 2
print(27//10) #나머지 7
print(type(10/27)) #float
print(type(10/27))  #int
print(type(10/27))  #float

#변수 이름 규칙, 자료형 변환
#my_mbti, my_function, myClass #myMbti : camel-case,my_mbti : snake-case

my_mbti = 'INFP'
print(f'my_mbti: ${my_mbti}')


print(f'my_mbti: '+my_mbti+'age'+str(age)) #java : String.toString(age); , python : str(age)
height = '176.6'

print(float(height) + 10) #java : Float.perseFloat(height); python : float(height)

#str(), int(), float() : 자료형 변환 함수
# + 연산자 : 숫자 + 숫자 => 덧셈, 문자 + 문자 => 문자문자
# * 연산자 : 숫자 * 숫자 => 곱셉, 문자 * 숫자 => 문자를 숫자만큼 반복

print(18+2) #20
print('18'+'2') #182
print(18*2) #36
print('2'*4) #'2222'

#짝을 10번 출력
print('짝' * 10)

print(18 ** 3) # ** -> 거듭제곱

#진수 #java:8진수 0o; 16진수0x;
print(0b10) #2진수 10 -> 2
print(0o10) #8진수 10 -> 8
print(0x10) #10진수 10 -> 16
print(0xFF) #10진수 FF -> 255

#10진수 -> 2진수
print(bin(10)) #0b1010
print(bin(9)) #0b1001
print(oct(10)) #0o12
print(hex(10)) #0xa

#(Hong)지수 표현
print(f'지구의 나이: {4.543e9}살') #float
print(f'원자의 크기: {1e-10}살') #float

#복소수
print(9+1j-4-5j) #(-5-4j)
ys = 9+1j
hj = 7-3j
print(ys+hj) #(16-2j)
print(ys.real) #9.0
print(hj.real) #-3.0
print(hj.conjugate()) #켤레복소수
print(hj*hj.conjugate()) #(58+0j) = 49 + (-3j x 3j) = 49 + 9 = (58 + 0j)
print(type(ys))



