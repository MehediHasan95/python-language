# Python List
# In Python, lists are used to store multiple data at once.

subjects = ["C/C++", "Python", "JavaScript", "Java", "PHP", "React JS", "Laravel"]

print(subjects[3])  # Java
print(subjects[3:5])  # ['Java', 'PHP']
print(subjects[4:])  # ['PHP', 'React JS', 'Laravel']
print(subjects[-1])  # Laravel

matched_1 = "Python" in subjects
print(matched_1)  # True

matched_2 = "Swift" in subjects
print(matched_2)  # False

matched_3 = "Next JS" not in subjects
print(matched_3)  # True

matched_4 = "React JS" not in subjects
print(matched_4)  # False
