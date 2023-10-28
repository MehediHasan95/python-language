"""In computer programming, a string is a sequence of characters."""

university = "Stamford University Bangladesh"
print(len(university))  # length: 30

print(university[6])  # r

print(university[-4])  # d

print("u" in university)  # False
print("v" in university)  # True
print("U" not in university)  # False

print(university[9:20])  # University

# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

greet = "Hello"
for word in greet:
    print(word)
