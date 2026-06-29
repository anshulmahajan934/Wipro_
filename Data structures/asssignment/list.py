#Q1
numbers = [10, 20, 30, 40, 50]
print("Complete list:", numbers)
print("Element at index 0:", numbers[0])
print("Element at index 2:", numbers[2])
print("Element at index 4:", numbers[4])
#Q2
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
#Q3
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)
#Q4
numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20
occurrences = numbers.count(target)
print(occurrences)
#Q5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print(list2)
#Q6
numbers = [10, 20, 30, 40]
numbers.insert(1, 15)
print(numbers)
#Q7
numbers = [10, 20, 30, 40, 50]
removed_item = numbers.pop(2)
print("Updated list:", numbers)
print("Removed item:", removed_item)
#Q8
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
print(numbers)