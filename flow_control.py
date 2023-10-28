"""Python if...else Statement"""
rahim_age = 25
karim_age = 27

if rahim_age > karim_age:
    print("Rahim is elder brother.")
else:
    print("Karim is elder brother.")

"""Python for Loop"""
countries = [
    "Bangladesh",
    "India",
    "England",
    "Canada",
    "Argentina",
    "Brazil",
]
for country in countries:
    print(country)  # Bangladesh, India, England ...

"""Python while Loop"""
index = 0
while index < 10:
    print(index)  # 0, 1,2,3 ...
    index += 1

"""Python break and continue"""
ages = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# break
for age in ages:
    if age == 10:
        break
    print(age)  # 6,7,8,9

# continue
for age in ages:
    if age == 10:
        continue
    print(age)  # 11, 12,13,14 ...

# pass
n = 5.5
if n > 0.5:
    pass
