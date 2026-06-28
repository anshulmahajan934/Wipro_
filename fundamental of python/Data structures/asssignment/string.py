#Q1
text = "Hello World!"
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)
#Q2
text = "radar"
cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#Q3
text = "Wipro"
n = len(text)
copies = text[:2] * n
print(copies)
#Q4
text = "xHix"

if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]

print(text)
#Q5
text = "Wipro"
n = 3

last_n_chars = text[-n:] if n > 0 else ""
result = last_n_chars * n
print(result)