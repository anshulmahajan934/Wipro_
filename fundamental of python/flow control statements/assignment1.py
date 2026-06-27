
#Q1
a= int(input("Enter a number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Q2
b= int(input("Enter another number: "))
if b>0:
    print("The number is positive.")
elif b<0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
#Q3
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
if a%10==b%10:
    print("True")
else:
    print("False")
         
#Q4
for i in range(1, 11):
    print(i, end=" ")
#Q5
for i in range (23,58):
    if i%2==0:
       print(i)
       
#Q6
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
#Q7
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
#Q8
num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    remainder = num % 10 
    digit_sum += remainder 
    num = num // 10  
print("Sum of digits:", digit_sum)    
#Q9
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    remainder = num % 10  
    reversed_num = (reversed_num * 10) + remainder  
    num = num // 10  
print("Reversed number:", reversed_num)      
#Q10
original_num = int(input("Enter a number: "))
num = original_num
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")  
    