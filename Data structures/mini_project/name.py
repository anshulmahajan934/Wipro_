def count_alex(text):

    name = "Alex"
    
    
    total = text.count(name)
    
    return total


if __name__ == "__main__":
    
    input_text = "Hi Alex WelcomeAlex Bye Alex ."

    result = count_alex(input_text)
    

    print(result)