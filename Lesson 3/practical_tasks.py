def count_fruits(fruits, keyword):
    exact_count = fruits.count(keyword)
    partial_count = sum(keyword in fruit for fruit in fruits)
    return exact_count, partial_count


fruits = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']

user_input = input("Enter a fruit name: ")
exact, partial = count_fruits(fruits, user_input)

print("Exact count:", exact)
print("Partial count:", partial)
