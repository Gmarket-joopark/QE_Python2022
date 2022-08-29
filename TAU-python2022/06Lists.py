#list 는 자료 구조형
#다른 리스트도 넣을 수 있다.
#인덱스를 통해 자료를 찾을 수 있다.
fruits = ["peaches", "pears",  "apples"]
years = [3, "1998", 2.5, 987, "1994"]
#
# print(fruits, years)
#
fruits.append("oranges")
print(fruits)


fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

fruits.pop(0) #Python lists begin at 0.
print(fruits)
#fruits.sort()

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
print(numbers)

numbers.sort()

print("after sort :", numbers)


print("apples" in fruits)
print("5" in numbers) # 숫자와 글자 주의할 것
print(5 in numbers)


print(fruits.count("apples"))
print(numbers.count("apples"))
print(numbers.count(4))

fruits = ["peaches", "pears",  "apples","apples","apples"]
print(fruits.index("apples")+1, "번째 자리")  #첫 자리는 0이다.
print(fruits.count("apples"))