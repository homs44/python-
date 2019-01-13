
#리스트 시작 ===========================================================

# 인덱싱과 슬라이싱
# #inde   0  1  2  3  4
# ages = [11,22,31,43,51]

# print(ages[0]) #첫번째 아이템 인덱싱
# print(ages[-1]) #마지막 아이템 인덱싱

# #슬라이싱은 기존 배열로부터 부분 배열을 만드는 작업.

# print(ages[1:2]) #슬라이싱 index 1 이상 2 미만

# subAges = ages[1:3] #슬라이싱 index 1 이상 3 미만
# print(subAges)

# fromTwoToLast = ages[1:] # index 1부터 끝까지
# print(fromTwoToLast)


#배열 더하기, 배열 곱하기, 배열 길이(개수) 확인

# arr1 = [1,2,3]
# arr2 = [4,5,6]

# print(arr1+arr2) # 배열 더하기
# print(arr1 * 3) # 배열 곱하기

# numberOfArr = len(arr1) #배열 아이템 개수 확인
# print(numberOfArr)


# #배열 수정 및 삭제

# arr = [1,2,4,4,5,6,7]

# arr[2] = 3 #index가 2인 즉 3번째 아이탬을 3으로 변경

# print(arr)

# del arr[2] #배열 index 2인 아이탬 삭제

# print(arr)


# #배열 append

# arr = [1,2,3,4,5]

# arr.append(6)

# print( arr )



# # 배열 sort, reverse

# arr = [ 5,4,7,2,1]

# arr.sort()

# print(arr)

# arr.reverse()

# print(arr)


# # 배열 index, insert, remove

# arr = [2,1,7,8,4,5,6,99]

# print( arr.index(7) ) # 아이탬 7의 인덱스 

# arr.insert(3,99) # index 3에 99 추가

# print(arr)

# arr.remove(3) # 아이탬 99 삭제

# print(arr)



# # 배열 pop, count, extend

# arr = [1,2,3,4,5,6,3,3]

# last = arr.pop()
# print("마지막 아이템 "+str(last))
# print ( arr )

# count = arr.count(3)
# print("3의 개수 " + str(count))
# count = arr.count(8)
# print("8의 개수 " + str(count))


# print("현재 배열 : " +str(arr))
# arr.extend([1,2,3,4])
# print("extend이후 배열" + str(arr))

#리스트 종료 ===========================================================