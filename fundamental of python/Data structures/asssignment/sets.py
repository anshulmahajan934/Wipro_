#Q1
my_set = {10, 20, 30, 40, 50}
item_to_remove = 30
my_set.discard(item_to_remove)
print(my_set)

#Q2
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)
#Q3
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
#Q4
my_set = {45, 12, 89, 5, 23}
max_val = max(my_set)
min_val = min(my_set)
print("Maximum value:", max_val)
print("Minimum value:", min_val)