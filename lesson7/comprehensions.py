nums = [2,3,4,8,1,6]

squares = []
for num in nums:
    squares.append(num ** 2)

squares = [num**2 for num in nums]
numbers = [i for i in range(1, 101)]

nums_dict = {num: num**2 for num in nums}

cities = ['london', 'paris', 'jerusalem']
countries = ['uk', 'france', 'israel']
my_dict = {country: city for country, city in zip(countries, cities)}

print(my_dict)


new_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 101)]
# print(new_list)

num = 0
while num != 0:
    print("hi", num)
    num += 1
else:
    print("inside else")
print("bye")