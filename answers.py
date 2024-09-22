#task1
name = "Bobur"
print(name)

#task2
my_list = [10, 20, 30]
my_list[1] = 99
print(my_list)

#task3
a = 5
b = 7
result = a + b
print("Sum of numbers:", result)

#task4
text = "Ipak Yuli is a good bank. I am a customer of a good bank"
new_text = text.replace("a good", "the best")
print(new_text)

#task5
def multiply(x, y):
    return x * y
result = multiply(4, 5)
print("The function's result is:", result)

#task6
for i in range(1, 11):
    if i < 10:
        print(i, end=' ')
    else:
        print(i)

#task7
my_dict = {
    'key1': 'definition1',
    'key2': 'definition2',
    'key3': 'definition3'
}
my_dict['key2'] = 'new_definition'
print(my_dict)

#task8
my_tuple = (1, 'hello', 3.14, True)
print("The result is:", len(my_tuple))

#task9
number = 10
while number >= 1:
    print(number)
    number -= 1

#task10
def filter_even_numbers(numbers):
    # Используем list comprehension для фильтрации четных чисел
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers_list = filter_even_numbers(numbers_list)
print(even_numbers_list)

#task11
text = "This is just an example"
words = text.split()
for word in words:
    print(word)

#task12
my_set = set()
my_set.add(1)
my_set.add('apple')
my_set.add(3.14)
print(my_set)

#task13
text = "I'm the one who knocks the door"
index = text.find("who")
print(index)

#task14
def reverse_string(s):
    return s[::-1]
original_string = "Hello_World"
reversed_string = reverse_string(original_string)
print(reversed_string)

#task15
numbers = [5, 2, 9, 1, 7, 3]
numbers.sort()
print(numbers)

#task16
squares = [x**2 for x in range(1, 6)]
print(squares)

#task17
number = float(input("Enter number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

#task18
words = ["apple", "banana", "cherry"]
result = ",".join(words)
print(result)

#task19
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = 5
result = factorial(number)
print(f"Factorial of {number} is equal to {result}")

#task20
text = "Hello world!"
upper_text = text.upper()
print(upper_text)