#Q!
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
sample_list = (8, 2, 3, 0, 7)
print(sum_of_list(sample_list))  
#Q2
def reverse_string(text):
    return text[::-1]
sample_string = "1234abcd"
print(reverse_string(sample_string))  
#Q3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))  
#Q4
def count_case(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

count_case("The quick Brow Ny Fox")
#Q5
def print_even_numbers(numbers):
    even_list = [num for num in numbers if num % 2 == 0]
    print(even_list)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list) 
#Q6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))  
print(is_prime(4))   
