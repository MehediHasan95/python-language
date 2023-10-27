"""Lists is built-in data types in Python used to store collections of data"""


"""subjects: list = ["English", "Geography", "Science"]"""

subjects = ["Mathematics", "Geography", "Science"]
print(len(subjects))  # length: 3

"""append()
The append() method adds an item to the end of the list.
"""
subjects.append("Chemistry")
print(subjects)  # ['Mathematics', 'Geography', 'Science', 'Chemistry']

"""insert()
The insert() method inserts an element to the list at the specified index.
"""
subjects.insert(2, "Geography")
print(subjects)  # ['Mathematics', 'Geography', 'Geography', 'Science', 'Chemistry']

"""extend()
The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
"""
numbers = [1, 4]
prime_numbers = [2, 6, 8]
numbers.extend(prime_numbers)
print(numbers)  # [1, 4, 2, 6, 8]

"""sort()
The sort() method sorts the items of a list in ascending or descending order.
"""
stu_marks = [45, 78, 85, 56, 64, 39]
stu_marks.sort()
print(stu_marks)  # [39, 45, 56, 64, 78, 85]

"""reverse()
The reverse() method reverses the elements of the list.
"""
stu_marks.reverse()
print(stu_marks)  # [85, 78, 64, 56, 45, 39]

"""index()
The index() method returns the index of the specified element in the list.
"""
languages = ["Python", "Java", "JavaScript", "Swift", "Kotlin"]
pos = languages.index("Swift")
print(pos)  # 3

"""copy()
The copy() method returns a shallow copy of the list.
"""
new_language = languages.copy()
print(new_language)  # ["Python", "Java", "JavaScript", "Swift", "Kotlin"]

"""clear()
The clear() method removes all items from the list.
"""
languages.clear()
print(languages)  # []

"""count()
The count() method returns the number of times the specified element appears in the list.
"""
scoreboard = [4, 0, 0, 2, 1, 6, 1, 4, 4]
total_6 = scoreboard.count(6)
total_4 = scoreboard.count(4)
print(total_6, total_4)  # 1 3

"""pop()
The list pop() method removes the item at the specified index. The method also returns the removed item.
"""
scoreboard.pop()
print(scoreboard)  # [4, 0, 0, 2, 6, 1, 4, 4]

"""remove()
The remove() method removes the first matching element (which is passed as an argument) from the list.
"""
scoreboard.remove(6)
print(scoreboard)  # [4, 0, 0, 2, 1, 1, 4]
