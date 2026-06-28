#Q1
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("4th element from first:", my_tuple[3])
print("4th element from last:", my_tuple[-4])
#Q2
my_tuple = ("a", "b", "c", "d")
element = "c"

if element in my_tuple:
    print(f"Element '{element}' exists in the tuple.")
else:
    print(f"Element '{element}' does not exist.")
#Q3
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)
#Q4
my_tuple = (10, 20, 30, 40, 50)
item = 30
index = my_tuple.index(item)
print(f"Index of {item}:", index)
#Q5
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result_list = []

for t in sample_list:
    new_tuple = t[:-1] + (100,)
    result_list.append(new_tuple)

print(result_list)