def filter_even_numbers(numbers):
    # სიის ყველა ელემენტზე და შეინახავს მხოლოდ ლუწი რიცხვების სიაში
    even_numbers = [num for num in numbers if num % 2 == 0]
    # აბრუნებს სიის მხოლოდ ლუწი რიცხვების
    return even_numbers

# მაგალითი გამოყენება
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(numbers_list)
print(filtered_list)  # შედეგი: [2, 4, 6, 8, 10]




def filter_short_strings(strings):
    # სიის ყველა სტრინგზე და შეინახავს მხოლოდ იმ სტრინგებს, რომელთა სიგრძე <= 4
    short_strings = [s for s in strings if len(s) <= 4]
    # აბრუნებს სიის მხოლოდ მოკლე სტრინგების
    return short_strings

# მაგალითი გამოყენება
strings_list = ["apple", "bat", "dog", "cat", "elephant"]
filtered_list = filter_short_strings(strings_list)
print(filtered_list)  # შედეგი: ['bat', 'dog', 'cat']




def filter_integers(numbers):
    # filter ფუნქციის გამოყენებით აირჩევა მხოლოდ მთელი რიცხვები
    return list(filter(lambda x: isinstance(x, int), numbers))

# მაგალითი გამოყენება
numbers_list = [1, 2.5, 3, 4.0, 5, 6.7]
filtered_list = filter_integers(numbers_list)
print(filtered_list)  # შედეგი: [1, 3, 5]
