# Trip Planner Program

# Collect User Input

destination = input("Enter your destination: ")
total_distance = float(input("Enter the total distance in miles: "))
fuel_efficiency = float(input("Enter your car's fuel efficiency (mpg): "))
gas_price = float(input("Enter the current gas price per gallon: "))
num_nights = int(input("Enter the number of nights you'll stay: "))
hotel_cost_per_night = float(input("Enter the average hotel cost per night: "))
daily_food_budget = float(input("Enter your daily food budget: "))

# Calculations

gallons_needed = total_distance / fuel_efficiency
fuel_cost = gallons_needed * gas_price
hotel_total = num_nights * hotel_cost_per_night
food_total = num_nights * daily_food_budget
total_trip_cost = fuel_cost + hotel_total + food_total

# Output summary

print("\n---Road Trip Budget Summary---")
print(f"Destination: {destination}")
print(f"Fuel needed: {gallons_needed:.2f} gallons")
print(f"Fuel cost: ${fuel_cost:.2f}")
print(f"Hotel cost for {num_nights} nights: ${hotel_total:.2f}")
print(f"Food budget for {num_nights} days: ${food_total:.2f}")
print(f"-------------------------------")
print(f"Total estimated trip cost: ${total_trip_cost:.2f}")



