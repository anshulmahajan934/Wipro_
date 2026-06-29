#Q1
import sys

def main():
    if len(sys.argv) < 3:
        return

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total_sum = num1 + num2
        
        if total_sum.is_integer():
            print(int(total_sum))
        else:
            print(total_sum)
    except ValueError:
        pass

if __name__ == "__main__":
    main()
    
#Q2
import sys
import os

def main():
    if len(sys.argv) < 2:
        return

    file_name = os.path.basename(sys.argv[0])
    welcome_message = " ".join(sys.argv[1:])
    
    print(f"File Name: {file_name}")
    print(f"Message: {welcome_message}")

if __name__ == "__main__":
    main()
 #Q3
import sys

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

def main():
    if len(sys.argv) != 11:
        return

    prime_sum = 0
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            if is_prime(num):
                prime_sum += num
        except ValueError:
            pass

    print(f"Sum of prime numbers: {prime_sum}")

if __name__ == "__main__":
    main()