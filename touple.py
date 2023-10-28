"""Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples
once created cannot be modified. In Python, a tuple is an immutable sequence type.
"""

tup = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print(tup[3])  # 20
print(tup[5:])  # (30, 35, 40, 45, 50)
print(tup[3:7])  # (20, 25, 30, 35)
print(tup[-1])  # 50

"""index()"""
name_tup = ("Mehedi", "Omi", "Shifa", "Mahi")
print(name_tup.index("Shifa"))  # 2

"""count()"""
age_list = (12, 14, 10, 11, 14, 15, 16, 15, 14, 12)
print(age_list.count(12))  # 2
print(age_list.count(14))  # 3

# for loop:
for age in age_list:
    print(age)

a = tuple(range(100, 110))
print(a)  # (100, 101, 102, 103, 104, 105, 106, 107, 108, 109)
