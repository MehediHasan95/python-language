countries = [
    "Bangladesh",
    "India",
    "England",
    "Australia",
    "Canada",
    "Argentina",
    "Brazil",
    "Dominican Republic",
]
# while loop:
index = 0
while index < len(countries):
    print(countries[index])
    index += 1

# for loop
for country in countries:
    print(country)

values = range(50, 101, 2)
for value in values:
    print(value)


# find large name from countries:
large_country_name = ""
for country in countries:
    total_word = len(country)
    if total_word > len(large_country_name):
        large_country_name = country

print(large_country_name)  # Dominican Republic


# remove duplicate elements from a list:
marks = [33, 35, 36, 35, 33, 39, 40, 39, 38]
unique = []
for mark in marks:
    total_matched = unique.count(mark)
    if total_matched == 0:
        unique.append(mark)

print(unique)  # [33, 35, 36, 39, 40, 38]


# sum of total marks:
total_marks = 0
for mark in marks:
    total_marks += mark

print(total_marks)  # 328
