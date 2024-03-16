# name = input("What is yoyur name? ")
# print(f"Hello, {name}!")

def input_two_numbers():
    global num1
    global num2
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))


def sum_of_numbers(num1, num2):
    result = num1 + num2
    return result


def number_difference(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    return result


def product_of_numbers(num1, num2):
    Result = num1 * num2
    return Result

# print(type(num1), type(num2))
# sum = num1 + num2
# print(f"Result = {sum}")

# if num1 > num2:
#     print(f"{num1} > {num2}")
# elif num1 < num2:
#     print(f"{num1} < {num2}")
# else:
#     print(f"{num1} = {num2}")


print("\t\t\tNothing\n\t\t\twill work\n\t\t\tunless you do")
print("")
print("\t\"Anyone who\n\t   stops\n\t      learning is old,\n\t         whether at twenty or eighty\"\n\t\t\t\t  Henry Ford")
print("")
input_two_numbers()
print("")
print(f"Sum of numbers:\n{sum_of_numbers(num1, num2)}\nNumber difference:\n{
      number_difference(num1, num2)}\nProduct of numbers:\n{product_of_numbers(num1, num2)}")
