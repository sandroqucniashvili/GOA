for i in range(1,11):
    print(i)



ds= "me miyvars fexburti"
dt= 5

for _ in range(dt):
    print(ds)


number = 1

while number <= 5:
    print(number)
    number += 1


    count = 0

while count < 3:
    print("hello")
    count += 1




age_str = input("Enter your age: ")


age = int(age_str)
if age >= 0:
        print("Your age is positive.")
else:
        print("Your age is negative.")




user_input = input("შეიყვანეთ რიცხვი: ")
number = int(user_input)


if number == 10:
    print(f"რიცხვი {number}-ს ტოლია 10-ს.")
else:
    print(f"რიცხვი {number}-ს არ ტოლია 10-ს.")
    



user_input = input("შეიყვანეთ რიცხვი: ")
number = int(user_input)

if number > 0 and number < 10:
    print("child")




side1 = float(input("შეიყვანეთ პირველი გვერდი: "))
side2 = float(input("შეიყვანეთ მეორე გვერდი: "))
side3 = float(input("შეიყვანეთ მესამე გვერდი: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("შესაძლებელია ამ გვერდებით სამკუთხედის აწყობა.")
else:
    print("არ შესაძლებელია ამ გვერდებით სამკუთხედის აწყობა.") 