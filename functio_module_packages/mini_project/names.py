import string_utils

name1 = "bob"
print("Sample input 1:", name1)
print("Sample output 1:")
print(string_utils.ispalindrome(name1))
print(string_utils.count_the_vowels(name1))
print(string_utils.frequency_of_letters(name1))

print("-" * 40)

name2 = "marcel bentok tanaka"
print("Sample input 2:", name2)
print("Sample output 2:")
print(string_utils.ispalindrome(name2))
print(string_utils.count_the_vowels(name2))
print(string_utils.frequency_of_letters(name2))