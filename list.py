"""Lists is built-in data types in Python used to store collections of data. List has mutable nature"""

subjects = ["Mathematics", "Geography", "Science"]
print(len(subjects))  # length: 3

serial_numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(serial_numbers[5])  # 30
print(serial_numbers[6:])  # [35, 40, 45, 50]
print(serial_numbers[2:6])  # [15, 20, 25, 30]
print(serial_numbers[-1])  # 50

"""append()"""
subjects.append("Chemistry")
print(subjects)  # ['Mathematics', 'Geography', 'Science', 'Chemistry']

"""insert()"""
subjects.insert(2, "Geography")
print(subjects)  # ['Mathematics', 'Geography', 'Geography', 'Science', 'Chemistry']

"""extend()"""
numbers = [1, 4]
prime_numbers = [2, 6, 8]
numbers.extend(prime_numbers)
print(numbers)  # [1, 4, 2, 6, 8]

"""sort()"""
stu_marks = [45, 78, 85, 56, 64, 39]
stu_marks.sort()
print(stu_marks)  # [39, 45, 56, 64, 78, 85]

"""reverse()"""
stu_marks.reverse()
print(stu_marks)  # [85, 78, 64, 56, 45, 39]

"""index()"""
languages = ["Python", "Java", "JavaScript", "Swift", "Kotlin"]
pos = languages.index("Swift")
print(pos)  # 3

"""copy()"""
new_language = languages.copy()
print(new_language)  # ["Python", "Java", "JavaScript", "Swift", "Kotlin"]

"""clear()"""
languages.clear()
print(languages)  # []

"""count()"""
scoreboard = [4, 0, 0, 2, 1, 6, 1, 4, 4]
total_6 = scoreboard.count(6)
total_4 = scoreboard.count(4)
print(total_6, total_4)  # 1 3

"""pop()"""
scoreboard.pop()
print(scoreboard)  # [4, 0, 0, 2, 6, 1, 4, 4]

"""remove()"""
scoreboard.remove(6)
print(scoreboard)  # [4, 0, 0, 2, 1, 1, 4]
