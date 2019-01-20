
"""

논리식



num1 = 10 
num2 = 11


num1 == num2 #False
num1 < num2 #True
num1 > num2 #False
num1 <= num2 #True
num1 >= num2 #False
num1 != num2 # True


name1 = "abc"
name2 = "bbb"

name1 == name2 #False
name1 != name2 #True

is

is not


and

or

"""


# 이름이 Jin  : 외상값 내놔!
# 이름이 Jack : 매일 먹던 거?
# Jin 또는 Jack이 아닐때 : 처음오셨어요?


# name = input("이름을 입력하세요 : ")

# # name  사용자 입력한 어떤 값이 문자열로 들어있음.

# if name == "Jin":
#     print("외상값 내놔!")
# elif name == "Jack":
#     print("매일 먹던 거?")
# else:
#     print("처음 오셨어요?")


"""
체중 kg
신장 m
bmi = 체중 / (신장*신장)

체중 80 
신장 1.8

bmi =  80 / (1.8 * 1.8)

25이하는 정상

25초과는 비만

"""

# weight = float(input("체중을 입력하세요(kg) : "))
# height = float(input("신장을 입력하세요(m) : "))

# bmi = weight / (height*height)

# if bmi<=25:
#     print("정상")
# else:
#     print("비만")


"""

while
특정 신호 받을때 대기 
무한정 반복 해야 될 때 

"""

# case 특정 신호를 받을 때 


# 외부로부터 어떤 시그널을 받아야될 때 

# 택배가 왔는지 계속 확인
# 택배가 왔으면 냉장고로 넣어야되요 
# 끝.


# isArrived = True

# while True:
#     if isArrived == True:
#         break


# case 무한정 반복해야 될 때

# 온도가 10미만이면 히터를 켜라
# 히터 켜져있을 때는 히터 켜지말라

# 온도가 10이상 30 미만이면 다 꺼라

# 온도가 30 이상이면 에어컨을 켜라
# 에어컨 켜져있을 때는 에어컨 켜지말라


# heater = False
# aircon = False
# currentTemparature = 15

# while True:
#     currentTemparature = int(input("현재 온도 : "))
#     if currentTemparature < 10 and heater == False:
#         heater = True
#         print("히터 on")
#     elif currentTemparature>=10 and currentTemparature < 30:
#         heater = False
#         aircon = False
#         print("다 꺼라")
#     elif currentTemparature>=30 and aircon == False:
#         aircon = True
#         print("에어컨 on")
#     else:
#         print("noting")







# message가 "Hi"이면  "Nice to meet you" 출력
# message가 "bye"이면 "Bye!"를 출력하고 프로그램 종료
# message가 "Hi또는 Bye"가 아니다 그러면 message를 그대로 출력 


#실행결과

# 메시지를 입력하세요 : Hi
# Nice to meet you
# 메시지를 입력하세요 : Hello
# Hello
# 메시지를 입력하세요 : Who are you?
# Who are you?
# 메시지를 입력하세요 : bye
# Bye!
# 프로그램 종료

# while True:
#     message = input("메시지를 입력하세요 : ")

#     if message.lower() == "hi":
#         print("Nice to meet you")
#     elif message.lower() =="bye":
#         print("Bye!")
#         break
#     else:
#         print(message)


# isNotOkay = True
# num = 0
# while isNotOkay:
#     # do someting
#     num = num + 1
#     if num > 10:
#         isNotOkay = False 


"""

For 

Iterable하다는 것은 아이템을 하나씩 꺼낼 수 있다.

"""

tup = (1, 2, 3, 4, 5)
s = {1, 2, 2, 2, 3}
dic = {
    "name":"jack",
    "age":11,
    "address":"secret"
}

arr = [1, 2, 3, 4, 5]


# for item in arr:
#     print(item)

# for item in tup:
#     print(item)

# for item in s:
#     print(item)

# for key in dic:
#     print("{0} : {1}".format(key, dic[key]))


# users = [
#     {
#         "name":"Jack"
#     },
#     {
#         "name":"Joi"
#     },
#     {
#         "name":"Jin"
#     }
# ]

# for index in range(len(users)):
#     print("{0}번 유저는 {1}".format(index+1, users[index]["name"])) # 1번째 유저는 {name}입니다.

# for item in range(1,10):
#     print(item)

# for i in range(1,10):
#     # i = 1
#     for j in range(1,10):
#         #j = 0
#         print("{0} X {1} = {2}".format(i, j, i*j))




#  *****
#  *****
#  *****
#  *****
#  *****

# for i in range(5):
#     print("*****")

# print("*", end="")


# *
# **
# ***
# ****
# *****

