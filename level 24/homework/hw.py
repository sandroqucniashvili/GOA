def find_longest_string(strings):
    # შეამოწმე, თუ სია ცარიელია
    if not strings:
        return None  # ან შეგიძლიათ დააბრუნოთ სხვა მნიშვნელობა ან მესიჯი
    
    # პირველ სტრინგს აღჭურვოს როგორც ყველაზე გრძელი სტრინგი
    longest_string = strings[0]
    
    # გაიარეთ სიის ყველა სტრინგზე
    for s in strings:
        # შეამოწმე, არის თუ არა მიმდინარე სტრინგი უფრო გრძელი ვიდრე ყველაზე გრძელი
        if len(s) > len(longest_string):
            # განაახლეთ ყველაზე გრძელი სტრინგი
            longest_string = s
    
    # აბრუნებს ყველაზე გრძელი სტრინგი
    return longest_string

# მაგალითი გამოყენება
strings_list = ["apple", "banana", "cherry", "date"]
longest_string = find_longest_string(strings_list)
print(longest_string)  # შედეგი: 'banana'









def process_numbers(numbers):
    # ახალი სია, სადაც შევინახავთ დამუშავებული რიცხვები
    processed_numbers = []
    
    # გაიარეთ სიის ყველა რიცხვზე
    for num in numbers:
        if num % 2 == 0:
            # თუ რიცხვი ლუწია, გაამრავლეთ იგი თავის თავზე
            processed_numbers.append(num * num)
        else:
            # თუ რიცხვი კენტია, 2-ს დაამატეთ და დაამატეთ სიაში
            processed_numbers.append(num + 2)
    
    # აბრუნებს ახალ სიის, სადაც გაწვდილი და დამატებული რიცხვებია
    return processed_numbers

# მაგალითი გამოყენება
numbers_list = [1, 2, 3, 4, 5]
processed_list = process_numbers(numbers_list)
print(processed_list)  # შედეგი: [3, 4, 5, 16, 7]
