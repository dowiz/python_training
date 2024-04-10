# def count_fruits(fruits, keyword):
#     exact_count = fruits.count(keyword)
#     partial_count = sum(keyword in fruit for fruit in fruits)
#     return exact_count, partial_count


# fruits = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']

# user_input = input("Enter a fruit name: ")
# exact, partial = count_fruits(fruits, user_input)

# print("Exact count:", exact)
# print("Partial count:", partial)

# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є у всіх кортежах:

tuple1 = (1, 3, 2, 6, 4, 5)
tuple2 = (2, 3, 4, 5, 4, 5)
tuple3 = (3, 4, 5, 6, 4, 5)

common_elements = set(tuple1) & set(tuple2) & set(tuple3)
print("Common elements:", common_elements)

# Завдання 2
unique_elements = set(tuple1) ^ set(tuple2) ^ set(tuple3)
print("Unique elements:", unique_elements)

# Завдання 3
# common_elements_at_same_position = [x for x in zip(
#     tuple1, tuple2, tuple3) if len(set(x)) == 1]
common_elements_at_same_position = [set(x) for x in zip(
    tuple1, tuple2, tuple3) if len(set(x)) == 1]
print("Common elements at same position:", common_elements_at_same_position)
