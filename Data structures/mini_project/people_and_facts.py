facts_dict = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

for person, fact in facts_dict.items():
    print(f"{person}: {fact}")

print()


change_name = input("Whose fact would you like to change? ")
if change_name in facts_dict:
    new_fact = input(f"Enter the new fact for {change_name}: ")
    facts_dict[change_name] = new_fact
else:
    print(f"{change_name} is not in the dictionary.")


add_name = input("\nEnter the name of a new person to add: ")
add_fact = input(f"Enter the fact for {add_name}: ")
facts_dict[add_name] = add_fact

print()

for person, fact in facts_dict.items():
    print(f"{person}: {fact}")