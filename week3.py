
a = 10

if a > 5 : 
    print(a)
    print(a)

    print('끝')

password = 'data'
answer = input('비밀번호를 입력해주세요:')

if( answer == password ) : print('correct')
    
num = int(input('숫자 하나 입력해주세요'))

if():
    print('짝수')

math = 83
science = 90

if math >= 80 and science >= 80 :
    print('합격')

math = 83
science = 90

if math < 80 or science < 80:
    print('탈락')

num = int(input('숫자 입력 : '))

if( num %5 == 0 and num %7 == 0 ):
    print('35의 배수')

if ( 10%num == 0 and 15 % num == 0 ) :
    print ('10과 15의 공약수')

if a > 5 :
    pass

print('끝')

math = 83
science = 90

if ( math < science ) :
    print (math)
else : 
    print : science

num = int(input('숫자 입력:'))

if (num%2 == 0 and num > 10 ):
    print('x')
else:
    print('o')


year = int(input("연도를 입력하세요: "))

if (year%4 == 0 and year %100 !=0) or year %400 == 0 :
    print ("%d년은 윤년입니다."%year)
else:
    print("%d년은 윤년이 아닙니다"%year)    

if score > 90:
    print('a')
elif score > 80:
    print('b')
elif score > 70:
    print('c')
elif score > 60:
    print('d')
else :
    print('f')

if price >= 50000:
    print ('배달비무료')
elif price >= 30000:
    delivery_fee = price * 0.05
elif price >= 10000:
    delivery_fee = price * 0.1
else:
    print ('베달 불가')

print('배달비는 %d원'%delivery_fee)

if speed > 100:
    print('위험')
elif speed > 80:
    print('과속')
elif speed > 50:
    print('속도줄이세요')

answer = 42
user_number = int(input("1부터 100 사이의 숫자를 입력하세요"))

if answer > user_number:
    print ("더 큰 숫자를 입력하세요!")
elif answer < user_number:
    print("더 작은 숫자를 입력하세요!")
else:
    print("정답입니다! 축하합니다!")