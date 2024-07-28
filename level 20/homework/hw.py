def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(sum_of_even_numbers(numbers))  





def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


string = "hello"
print(reverse_string(string))  



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = 5
print(factorial(number))  





def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
print(common_elements(list1, list2)) 



def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


string = "hello world"
print(count_vowels(string))  


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


integers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(integers)) 




def are_permutations(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
print(are_permutations(string1, string2))




def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


number = 29
print(is_prime(number))





def sort_by_length(strings):
    return sorted(strings, key=len)


strings = ["apple", "banana", "cherry", "date"]
print(sort_by_length(strings))