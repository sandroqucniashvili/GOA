# ჯამი შეცვლისთვის
sum_of_even_numbers = 0

# 0-დან 10-მდე რიცხვების მონათვლა
for number in range(11):  # range(11) გამოიტანს რიცხვებს 0-დან 10-მდე
    if number % 2 == 0:  # 
        sum_of_even_numbers += number  # ლუწი რიცხვის დამატება ჯამში

# დაბეჭდეთ ლუწი რიცხვების ჯამი
print("ლუწი რიცხვების ჯამი:", sum_of_even_numbers)



# ჯამი შეცვლისთვის
sum_of_odd_numbers = 0

# 0-დან 10-მდე რიცხვების მონათვლა
for number in range(11):  # range(11) გამოიტანს რიცხვებს 0-დან 10-მდე
    if number % 2 != 0:  
        sum_of_odd_numbers += number  # კენტი რიცხვის დამატება ჯამში

# დაბეჭდეთ კენტი რიცხვების ჯამი
print("კენტი რიცხვების ჯამი:", sum_of_odd_numbers)




# ჯამი შეცვლისთვის
sum_of_multiples_of_5 = 0

# 0-დან 100-მდე რიცხვების მონათვლა
for number in range(101):  # range(101) გამოიტანს რიცხვებს 0-დან 100-მდე
    if number % 5 == 0:  
        sum_of_multiples_of_5 += number  # 5-ის ჯერადი რიცხვის დამატება ჯამში

# დაბეჭდეთ 5-ის ჯერადი რიცხვების ჯამი
print("5-ის ჯერადი რიცხვების ჯამი:", sum_of_multiples_of_5)



# 0-დან 100-მდე რიცხვების მონათვლა
print("3-ის ჯერადი რიცხვები 0-დან 100-მდე:")

for number in range(101):  # range(101) გამოიტანს რიცხვებს 0-დან 100-მდე
    if number % 3 == 0:  
        print(number)



# 20-დან 0-მდე რიცხვების უკუღმა გამოშვება
for number in range(20, -1, -1):  # range(start, stop, step)
    print(number)



# მომხმარებლისგან ორი რიცხვის მიღება
start_number = int(input("შეიყვანეთ პირველი რიცხვი: "))
end_number = int(input("შეიყვანეთ მეორე რიცხვი: "))

# დარწმუნდით, რომ start_number უფრო მცირეა end_number-ისგან
if start_number > end_number:
    start_number, end_number = end_number, start_number

# ჯამი შეცვლისთვის
sum_of_numbers = 0

# rიცხვების მონათვლა მოცემულ დიაპაზონში
for number in range(start_number, end_number + 1):
    sum_of_numbers += number

# დაბეჭდეთ რიცხვების ჯამი
print("რიცხვების ჯამი:", sum_of_numbers)




# ჯამი შეცვლისთვის
sum_of_even_numbers = 0

# წამოსაწყები რიცხვი
number = 0

# while ციკლი 0-დან 10-მდე რიცხვების გაწვდვისთვის
while number <= 10:
    if number % 2 == 0: 
        sum_of_even_numbers += number  # ლუწი რიცხვის დამატება ჯამში
    number += 1  # წასვლა შემდეგ რიცხვზე

# დაბეჭდეთ ლუწი რიცხვების ჯამი
print("ლუწი რიცხვების ჯამი:", sum_of_even_numbers)




# ჯამი შეცვლისთვის
sum_of_odd_numbers = 0

# წამოსაწყები რიცხვი
number = 0

# while ციკლი 0-დან 10-მდე რიცხვების გაწვდვისთვის
while number <= 10:
    if number % 2 != 0: 
        sum_of_odd_numbers += number  # კენტი რიცხვის დამატება ჯამში
    number += 1  # წასვლა შემდეგ რიცხვზე

# დაბეჭდეთ კენტი რიცხვების ჯამი
print("კენტი რიცხვების ჯამი:", sum_of_odd_numbers)


# ჯამი შეცვლისთვის
sum_of_multiples_of_5 = 0

# წამოსაწყები რიცხვი
number = 0

# while ციკლი 0-დან 100-მდე რიცხვების გაწვდვისთვის
while number <= 100:
    if number % 5 == 0:  
        sum_of_multiples_of_5 += number  # 5-ის ჯერადი რიცხვის დამატება ჯამში
    number += 5  # წასვლა შემდეგ 5-ის ჯერად რიცხვზე

# დაბეჭდეთ 5-ის ჯერადი რიცხვების ჯამი
print("5-ის ჯერადი რიცხვების ჯამი:", sum_of_multiples_of_5)


# წამოსაწყები რიცხვი
number = 0

# while ციკლი 0-დან 100-მდე რიცხვების გაწვდვისთვის
print("3-ის ჯერადი რიცხვები 0-დან 100-მდე:")

while number <= 100:
    if number % 3 == 0: 
        print(number)
    number += 1  # წასვლა შემდეგ რიცხვზე


# წამოსაწყები რიცხვი
number = 20

# while ციკლი 20-დან 0-მდე რიცხვების გაწვდვისთვის
while number >= 0:
    print(number)
    number -= 1  # წასვლა შემდეგ რიცხვზე უკუღმა



# სწორი პაროლი
correct_password = "password123"

# პაროლის შეყვანა და გადამოწმება
while True:
    # მომხმარებლისგან პაროლის მიღება
    entered_password = input("შეიყვანეთ პაროლი: ")
    
    # შემოწმება, არის თუ არა პაროლი სწორი
    if entered_password == correct_password:
        print("პაროლი სწორია.")
        break  # ციკლის გაწყვეტა სწორი პაროლის შემთხვევაში
    else:
        print("პაროლი არასწორია, სცადეთ თავიდან.")

