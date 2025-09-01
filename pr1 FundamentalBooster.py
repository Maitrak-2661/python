# Project: Fundamental Booster
# Student: Dev
# No functions used.


print("Personal Form for Dev")

username = input("Enter name: ")
ageNum = int(input("Enter age: "))
meters = float(input("Enter height in meters: "))
favDigit = int(input("Favourite number: "))

bYear = 2025 - ageNum

print(f"\nusername: {username} | type: {type(username)} | id: {id(username)}")
print(f"ageNum: {ageNum} | type: {type(ageNum)} | id: {id(ageNum)}")
print(f"meters: {meters} | type: {type(meters)} | id: {id(meters)}")
print(f"favDigit: {favDigit} | type: {type(favDigit)} | id: {id(favDigit)}")

print(f"\nApprox birth year: {bYear}")
print("Thanks!")
