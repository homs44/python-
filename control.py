"""

bmi 계산 프로그램

체중 / ( 신장(m) * 신장(m) )

18.5이하 저체중
18.5 ~ 23 정상
23 ~ 25  과체중
25 ~ 30 비만
30이상 고도비만

# """

# weight = float(input("몸무게를 입력하세요(kg) :"))
# height = float(input("신장을 입력하세요(m) :"))

# bmi = weight / (height*height)

# #제어문
# #if else 
# if bmi<=18.5:
#     print("당신의 bmi는 {0}이고 저체중입니다.".format(bmi))
# elif bmi<=23:
#     print("당신의 bmi는 {0}이고 정상입니다.".format(bmi))
# elif bmi<=25:
#     print("당신의 bmi는 {0}이고 과체중입니다.".format(bmi))
# elif bmi<=30:
#     print("당신의 bmi는 {0}이고 비만입니다.".format(bmi))
# else:
#     print("당신의 bmi는 {0}이고 고도비만입니다.".format(bmi))



# num1 = 10
# num2 = 10

# if num1==num2:
#     print("True 입니다.")
# else:
#     print("False 입니다.")



# 반복문
# while

# condition = True
# num = 1

# while condition:
#     print("number is {0}".format(num))
#     num = num+1

#     if num > 10:
#         break

# print("done")

# for

arr = [1,2,3,4,7]

# length = len(arr) #5
# index = 0

# while index<length:
#     print("number is {0}".format(arr[index]))    
#     index = index+1


# for item in arr:
#     print("number is {0}".format(item))

# print("done")

users = [
    {
        "name":"ingyu",
        "age":15
    },
    {
        "name":"jin",
        "age":17
    },
    {
        "name":"joi",
        "age":10
    }
]

# 나이가 15이하인 사람만 이름 출력
#ingyu
#joi

# for user in users:
#     if user["age"]<=15:
#         print(user["name"])




# 나이가 15이하인 사람들의 평균 나이를 구하라
# 평균 = n명 나이 총합 / n 

# sum = 0
# count = 0

# for user in users:
#     if user["age"]<=15:
#         sum = sum + user["age"]
#         count = count + 1


# avg = sum / count

# print("15이하인 사람들의 평균 나이는 {0}".format(avg))


# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()


