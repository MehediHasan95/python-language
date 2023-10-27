"""The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."""

serial_numbers_1 = range(10)
print(serial_numbers_1)  # range(0, 10)

serial_numbers_2 = range(10, 30)
print(serial_numbers_2)  # range(10, 30)

serial_numbers_3 = list(range(10))
print(serial_numbers_3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

serial_numbers_4 = list(range(10, 20))
print(serial_numbers_4)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

even_number = list(range(0, 11, 2))
print(even_number)  # [0, 2, 4, 6, 8, 10]

odd_number = list(range(0, 11, 3))
print(odd_number)  # [0, 3, 6, 9]
