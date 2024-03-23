fruits = ["apple", "banana", "True", "cherry", "34", ["test", 100], "Demo"]

# print("=====================================")
# fruits[6] = "Python"

# for item in fruits:
#     print(item)

# Last element
print(fruits[-1])

# Length of the list
print(len(fruits))
print("===========append=====================")
fruits.append("TypeScript")
print(fruits)
print("===========insert=====================")
fruits.insert(2, "C++")
print(fruits)
print("===========pop=====================")
fruits.pop(1)
print(fruits)
print("===========remove=====================")
fruits.remove(["test", 100])
print(fruits)
print("===========reverse=====================")
fruits.reverse()
print(fruits)
print("===========sort=====================")
fruits.sort()
print(fruits)
