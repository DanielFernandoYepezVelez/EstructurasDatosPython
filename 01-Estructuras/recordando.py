names = ["daniel", "otro", "Fernanda"]
numbers = [1,2,3,4,5,6,1,1,1,7,8,9]

names.insert(3, "Arturo")
index_name = names.index("Fernanda")
number_one = numbers.count(1)

print(names)
print(index_name)
print(number_one)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)