def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = [5, 3, 8, 1, 2]
print(find_min(numbers))


def find_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [5, 3, 8, 1, 2]
print(find_max(numbers))




def print_indices(my_list):
    indices = [1, 3, 5]
    for index in indices:
        if index < len(my_list):
            print(f"Index {index}: {my_list[index]}")
        else:
            print(f"Index {index} is out of range")

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print_indices(my_list)



def merge_lists(int_list, str_list):
    merged = []
    max_len = max(len(int_list), len(str_list))
    
    for i in range(max_len):
        if i < len(int_list):
            merged.append(int_list[i])
        if i < len(str_list):
            merged.append(str_list[i])
    
    return merged

int_list = [1, 2, 3]
str_list = ['a', 'b', 'c', 'd']
print(merge_lists(int_list, str_list))




def separate_types(my_list):
    integers = []
    strings = []
    
    for item in my_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
    
    return integers, strings

my_list = [1, 'hello', 2, 'world', 3]
integers, strings = separate_types(my_list)
print(integers)
print(strings)




def sum_odd_even(my_list):
    odd_sum = 0
    even_sum = 0
    
    for num in my_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return odd_sum, even_sum

my_list = [1, 2, 3, 4, 5, 6]
odd_sum, even_sum = sum_odd_even(my_list)
print(f"Odd sum: {odd_sum}")
print(f"Even sum: {even_sum}")




def separate_odd_even(my_list):
    odd_numbers = []
    even_numbers = []
    
    for num in my_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers

my_list = [1, 2, 3, 4, 5, 6]
odd_numbers, even_numbers = separate_odd_even(my_list)
print(odd_numbers)
print(even_numbers)





def lengths_of_strings(strings):
    lengths = [len(s) for s in strings]
    return lengths

strings = ["apple", "banana", "cherry"]
print(lengths_of_strings(strings))





def concatenate_and_sum(my_list):
    combined_string = ""
    total_sum = 0
    
    for item in my_list:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            combined_string += item
    
    return combined_string, total_sum

my_list = [1, "hello", 2, "world", 3]
combined_string, total_sum = concatenate_and_sum(my_list)
print(combined_string)
print(total_sum)






def even_index_elements(my_list):
    even_indexed_elements = [my_list[i] for i in range(0, len(my_list), 2)]
    return even_indexed_elements

my_list = [10, 20, 30, 40, 50, 60]
print(even_index_elements(my_list))
