# 예약어X
# snake_case
# 내장함수와 이름이 같으면 에러는 안나지만, 내장 함수를 호출 할 수 없음
# def sum(x):
#     print(x)
a = sum([10, 20, 3])
print(a)
print('-' * 20)
'''
자바
접근제어자 리턴형 함수명(파라미터1, 파라미터) {
    return 값;
}

파이썬
def 함수명(파라미터1, 파라미터2):
    return 값
'''


def my_print(age):
    print('정가현 : ' + str(age) + '살 입니다')
    print('정가현 : ', age, '살 입니다')
    print(f'정가현 : {age}살 입니다')


def my_print2(name, age):
    print(name + ' : ' + age + '살 입니다')
    print(name, ': ', age, '살 입니다')
    print(f'{name} : {age}살 입니다')


def my_print3(name, age, group):
    print(name + ' : ' + age + '살 입니다' + group + '소속입니다.')
    print(name, ': ', age, '살 입니다', group, ' 소속입니다.')
    print(f'{name} : {age}살 입니다 {group} 소속입니다')

my_print3(age=27, name='이지훈', group='세븐틴')
# my_print3(age=27,'이지훈','세븐틴') #키워드 인자 뒤에는 계속 키워드 인자 해야함, 위치 인자는 무조건 키워드 인자 앞에 있어야 한다
print(my_print(18))  # my_print() 실행, my_print()의 리턴값 출력
print(my_print2('이지훈', 27))
print(my_print2(age=27, name='이지훈'))
print('-' * 20)


def my_print4(name, age, group='세븐틴'):  # 기본값있는 파라미터
    print(name + ' : ' + age + '살 입니다' + group + '소속입니다.')
    print(name, ': ', age, '살 입니다', group, ' 소속입니다.')
    print(f'{name} : {age}살 입니다 {group} 소속입니다')


my_print4('이지훈', age=27, group='리더즈')
print('-' * 20)


# 가변인자
def my_print5(*args):
    print('정보 : ')
    for arg in args:
        print(arg)

def my_print6(name, *args):
    print('정보 : ')
    for arg in args:
        print(arg)

my_print5('이지훈', 27, '세븐틴', 'Ruby')
my_print6('이지훈', 27, '세븐틴', 'Ruby')
print('-' * 20)
print('-' * 20)
print('-' * 20)
