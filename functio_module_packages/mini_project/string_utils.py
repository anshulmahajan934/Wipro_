def ispalindrome(name):
    cleaned = name.replace(" ", "").lower()
    
    if cleaned == cleaned[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in name:
        if char in vowels:
            count += 1
            
    return f"No of vowels: {count}"


def frequency_of_letters(name):
    cleaned = name.replace(" ", "").lower()
    
    frequencies = {}
    
    for char in cleaned:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
            
    output_parts = []
    for char, count in frequencies.items():
        output_parts.append(f"{char} - {count}")
        
    return "Frequency of letters: " + ", ".join(output_parts)