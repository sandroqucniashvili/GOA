for i in range(21):
    print(i)


for i in range(1, 11):
    print(i)



print("Even numbers:")
for i in range(101):
    if i % 2 == 0:
        print(i)

print("Odd numbers:")
for i in range(101):
    if i % 2 != 0:
        print(i)


num = int(input("Enter a number: "))


total_sum = 0

for i in range(1, num + 1):
    total_sum += i

print(f"The sum of all numbers up to {num} is {total_sum}.")





for i in range(1, 51):
    if i % 5 == 0:
        print(i)





number = 2

while number <= 20:
    print(number)
    number += 2




total_sum = 0
number = 1


while number <= 10:
    total_sum += number
    number += 1

print(f"The sum of numbers from 1 to 10 is {total_sum}.")





correct_number = 7
guess = 0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_number:
        print("Wrong guess. Try again!")

print("Congratulations! You guessed the number correctly.")







numbers = [1, 2, 3, 4, 5]
doubled_numbers = []


index = 0
while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Doubled numbers:", doubled_numbers)





correct_password = "password123"
entered_password = ""


while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    if entered_password != correct_password:
        print("Incorrect password. Try again!")

print("Password accepted.")





current_hour = int(input("Enter the current hour (0-23): "))


if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")





temperature = float(input("Enter the temperature in degrees: "))


if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")





age = int(input("Enter your age: "))


if 13 <= age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")








sum_of_numbers = 0
for i in range(1, 11):
    sum_of_numbers += i
print("The sum of numbers from 1 to 10 is:", sum_of_numbers)






for i in range(1, 16):
    print(f"The square of {i} is {i ** 2}")







sum_of_squares = 0
for i in range(1, 6):
    sum_of_squares += i ** 2
print("The sum of squares from 1 to 5 is:", sum_of_squares)









print("Numbers divisible by both 3 and 5 from 1 to 100:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)




print("Numbers from 10 to 1 in reverse order:")
for i in range(10, 0, -1):
    print(i)






number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10 
    sum_of_digits += digit  
    number //= 10  

print("The sum of the digits is:", sum_of_digits)





count = 10

while count > 0:
    print(count)
    count -= 1








total_sum = 0
num = 1

while num <= 100:
    total_sum += num 
    num += 1  

print("The sum of all integers from 1 to 100 is:", total_sum)











num = 1

while num <= 10:
    print(f"The square of {num} is {num ** 2}")
    num += 1  








year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")










string = input("Enter a string: ")
cleaned_string = ''.join(string.split()).lower()

if cleaned_string == cleaned_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')


number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")








weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
