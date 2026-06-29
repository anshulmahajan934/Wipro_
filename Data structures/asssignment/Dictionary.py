#Q1
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)
#Q2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

print(result_dict)
#Q3
sample_dict = {"a": 100, "b": 200, "c": 300}
key_to_check = "b"

if key_to_check in sample_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist.")
#Q4
sample_dict = {"apple": 10, "banana": 20, "cherry": 30}

print("Keys alone:")
for key in sample_dict.keys():
    print(key)

print("\nValues alone:")
for value in sample_dict.values():
    print(value)

print("\nBoth keys and values:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
#Q5
square_dict = {}
for i in range(1, 16):
    square_dict[i] = i * i

print(square_dict)
#Q6
sample_dict = {"item1": 50, "item2": 150, "item3": 250}
total_sum = sum(sample_dict.values())
print("Sum of all values:", total_sum)

