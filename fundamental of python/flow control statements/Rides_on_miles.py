# Project 1 

distance = float(input("How far would you like to travel in miles? "))


if distance < 3:
    suggestion = "Bicycle"
elif distance < 300:
    suggestion = "Motor-Cycle"
else:
    suggestion = "Super-Car"
    
print(f"I suggest {suggestion} to your destination")
#Project 2
cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

print(f"How much does it cost to operate one server per day? ${cost_per_day:.2f}")
print(f"How much does it cost to operate one server per week? ${cost_per_week:.2f}")
print(f"How much does it cost to operate one server per month? ${cost_per_month:.2f}")

total_budget = float(input("Enter your total budget: "))
days_affordable = total_budget / cost_per_day

print(f"How many days can I operate one server with ${total_budget:.2f}? {int(days_affordable)} days")
