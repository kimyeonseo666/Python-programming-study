# print ('hello ,end=' ')
# print 


 ### 1번 문제
 # print (1,3,5,7,    )
 # print (1+3+5+7)

math = 92
science = 87
english = 94

print('수학,과학,영어 점수는 각각 %d점,%d점,%d점 입니다' %(math,science,english))
print("%s score: %d"%("math", math))
print("%s score: %d"%("science", science))
print("%s score: %d"%("english", english))


math = int(input('수학 점수: '))
python = int(input('파이썬 점수: '))
mean_score = float((math+python)/2)

print('수학 점수는 %s, 파이썬 점수는 %s 입니다.'%(math, python))
print('그리고 평균 점수는 %f점 입니다.'%mean_score)

a = 1
b = 5
c = a + b
print (c)
b = 9
c + a+b
print(c)

pi = 3.14159265
r = int(input('반지름:'))

length = 2*pi*r
area = pi*r**2
print ('원의 둘레는 %f, 넓이는 %f 입니다.' %(length,area))

a,b=2,3
print(a,b)


a = '동덕'
a += '여대'

print((a==5)or(b>100))

x = 150

print(100 < x) and (x < 200)