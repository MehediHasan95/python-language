"""In Python, a dictionary is a collection that allows us to store data in key-value pairs."""

products = {
    "name": "Mens Cotton Jacket",
    "price": 55.99,
    "category": "Men's clothing",
    "description": "A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day",
    "rating": {"rating": 4.5, "count": 500},
}

print(products.keys())  # show only keys or property name
print(products.values())  # show only values
print(products["name"])  # Mens Cotton Jacket
print(products["price"])  # 55.99

output_1 = products.get("rating")
print(output_1)  # {'rating': 4.5, 'count': 500}

country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London",
}

print(country_capitals["United States"])  # Washington D.C.
print(country_capitals["England"])  # London

output_2 = country_capitals.get("Italy")
print(output_2)  # Rome
