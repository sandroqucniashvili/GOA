example_str = "hello world"
upper_str = example_str.upper() 
example_str = "HELLO WORLD"
lower_str = example_str.lower()
example_str = "hELLO wORLD"
capitalize_str = example_str.capitalize()


my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list = ['apple', 'banana']
my_list.append('cherry')
print(my_list)

my_list = [10, 20, 30]
my_list.append(40)
print(my_list)


my_list = [1, 2, 3, 4]
popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list = ['apple', 'banana', 'cherry']
popped_element = my_list.pop(1)
print(popped_element)
print(my_list)

my_list = [10, 20, 30]
popped_element = my_list.pop(0)
print(popped_element)
print(my_list)


my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)

my_list = ['apple', 'cherry']
my_list.insert(1, 'banana')
print(my_list)

my_list = [10, 30]
my_list.insert(1, 20)
print(my_list)