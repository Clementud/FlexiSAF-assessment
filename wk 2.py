# PROFILE CARD
print("===== PROFILE CARD =====")

name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")
location = input("Enter your location: ")

print("\n--- Profile ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Location:", location)


# AGE CALCULATOR
print("\n===== AGE CALCULATOR =====")

birth_year = int(input("Enter your birth year: "))
current_year = 2026

calculated_age = current_year - birth_year

print("Your age is:", calculated_age)


# UNIT CONVERTER
print("\n===== UNIT CONVERTER =====")

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371

print(kilometers, "km =", round(miles, 2), "miles")


# RECEIPT TOTAL
print("\n===== RECEIPT TOTAL =====")

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

total = item1 + item2 + item3

print("Total: ₦", round(total, 2))


# SIMPLE INTEREST CALCULATOR
print("\n===== SIMPLE INTEREST CALCULATOR =====")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100
amount = principal + interest

print("Simple Interest: ₦", round(interest, 2))
print("Total Amount: ₦", round(amount, 2))