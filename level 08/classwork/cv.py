password1 = input("შეიყვანეთ პირველი პაროლი: ")
password2 = input("შეიყვანეთ მეორე პაროლი: ")

if password1 == password2:
    print("პაროლები ერთმანეთს ემთხვევა.")
else:
    print("პაროლები არ ემთხვევა.")


number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"{number1} < {number2} არის {number1 < number2}")
print(f"{number1} > {number2} არის {number1 > number2}")
print(f"{number1} <= {number2} არის {number1 <= number2}")
print(f"{number1} >= {number2} არის {number1 >= number2}")
print(f"{number1} == {number2} არის {number1 == number2}")

#N2


# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# შედარების ოპერაციები
less_than = num1 < num2
greater_than = num1 > num2
less_than_or_equal = num1 <= num2
greater_than_or_equal = num1 >= num2
equal_to = num1 == num2

# შედეგების გამოყვანა
print(str(num1) + " < " + str(num2) + " is " + str(less_than))
print(str(num1) + " > " + str(num2) + " is " + str(greater_than))
print(str(num1) + " <= " + str(num2) + " is " + str(less_than_or_equal))
print(str(num1) + " >= " + str(num2) + " is " + str(greater_than_or_equal))
print(str(num1) + " == " + str(num2) + " is " + str(equal_to))
#N3

# მომხმარებლისგან ერთი რიცხვის მიღება
num = float(input("Enter a number: "))

# შეამოწმეთ, არის თუ არა რიცხვი მეტი 5-ზე და ნაკლები ან ტოლი 10-ზე
if num > 5 and num <= 10:
    print("The number is greater than 5 and less than or equal to 10.")
else:
    print("The number is not in the range greater than 5 and less than or equal to 10.")

#N4
# მომხმარებლისგან რიცხვის მიღება
num = float(input("Enter a number: "))

# შეამოწმეთ, არის თუ არა რიცხვი მეტი 5-ზე ან მეტი 10-ზე
if num > 5 or num > 10:
    print("The number is greater than 5 or greater than 10.")
else:
    print("The number is not greater than 5 or greater than 10.")

#N5



# წვრილი თარიღი: true და false კომბინაციების შედეგები

# True და False ვახლებელი
true_value = True
false_value = False

#`and 
print("True and True:", true_value and true_value)        # True
print("True and False:", true_value and false_value)      # False
print("False and True:", false_value and true_value)      # False
print("False and False:", false_value and false_value)    # False

# or 
print("True or True:", true_value or true_value)          # True
print("True or False:", true_value or false_value)        # True
print("False or True:", false_value or true_value)        # True
print("False or False:", false_value or false_value)      # False
