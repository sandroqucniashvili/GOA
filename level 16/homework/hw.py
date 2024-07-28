
def pop_last_integer(lst):
    if lst:
        last_element = lst.pop()
        print(last_element)
    else:
        print("The list is empty.")

integers = [1, 2, 3, 4, 5]
pop_last_integer(integers)  


def pop_first_string(lst):
    if lst:
        return lst.pop(0)
    else:
        return "The list is empty."

strings = ["apple", "banana", "cherry"]
first_string = pop_first_string(strings)  
print(first_string)

def pop_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst.pop(index)
    else:
        return "Index out of range."

characters = ['a', 'b', 'c', 'd', 'e']
element_at_index_2 = pop_at_index(characters, 2)  
print(element_at_index_2)



def pop_last_element(lst):
    if lst:
        return lst.pop()
    else:
        return "The list is empty."

generic_list = [10, 20, 30, 40]
last_element = pop_last_element(generic_list)  
print(last_element)




def count_fives(lst):
    return lst.count(5)

integers = [1, 5, 3, 5, 5, 7]
count_of_fives = count_fives(integers)  
print(count_of_fives)





def count_letter_a(lst):
    return sum(s.count('a') for s in lst)

strings = ["apple", "banana", "cherry"]
count_a = count_letter_a(strings)  
print(count_a)




def count_true(lst):
    return lst.count(True)

booleans = [True, False, True, True, False]
count_true_values = count_true(booleans)  
print(count_true_values)







def count_sublists(nested_list, sublist):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            if item == sublist:
                count += 1
            else:
                count += count_sublists(item, sublist)
    return count

nested_list = [[1, 2], [3, 4], [5, [3, 4]], [[3, 4], [6, 7]], [3, 4]]
sublist = [3, 4]
count_of_sublists = count_sublists(nested_list, sublist)  
print(count_of_sublists)




integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


length_of_integers = len(integers)

print("List of integers:", integers)
print("Length of the list:", length_of_integers)




weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


number_of_weekdays = len(weekdays)

print("List of weekdays:", weekdays)
print("Number of weekdays:", number_of_weekdays)




nested_list = [[1, 2], [3, 4, [5, 6]], [7]]

total_elements = 0


to_visit = [nested_list]  
while to_visit:
    current_list = to_visit.pop() 
    for item in current_list:
        if isinstance(item, list):
            to_visit.append(item) 
        else:
            total_elements += 1  

print("Nested list:", nested_list)
print("Total number of elements in the nested list:", total_elements)


