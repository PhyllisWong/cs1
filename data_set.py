"""Data scraping using Python String Methods."""
"""
Questions for today’s File I/O problem:

4. What is the most popular payment type in Oakland in March?
5. How many sales were made on 4/20, which city had the highest sales value?
6. What is the average sales amount for credit card purchases?
7. How many purchases were made by bartering with baseball cards?
"""

"""
~~~~~~~~~~~~~~~~  Challenge 1  ~~~~~~~~~~~~~~~
1. What are the total amount of sales contained in this data set?
"""
# Read the file in python
with open("sales_data.txt", "r") as f:
    data = list(f)
    count = 0
    total = 0

    while count < len(data)-1:
        count += 1
        cell = data[count].split("\t")
        # cast the string numbers to a float, strip extra characters
        total += float(cell[3].strip("$\n"))
    # limit the decimals places to 2
    result = str(round(total, 2))
    # print(result)
# Answer is 500143918.36

"""
~~~~~~~~~~~~~~~~  Challenge 2  ~~~~~~~~~~~~~~~
2. Which city had the highest sales in February?
"""
# Open file, read each line, split on each "tab"
with open("sales_data.txt", "r") as f:
    listArr = list(f)
    cities = {}
    for line in listArr:
        arr = line.split('\t')
        date = arr[1]
        city = arr[0]
        amount = float(arr[3].strip("$\n"))
        if date.startswith("2"):
            if city in cities.keys():
                cities[city] += amount
            elif city not in cities.keys():
                cities[city] = amount
cities_key = max(cities, key=cities.get)
# print(cities_key)
# print("$" + str(round(cities[cities_key], 2)))
# Answer Boston $4320564.95

"""
~~~~~~~~~~~~~~~~  Challenge 3  ~~~~~~~~~~~~~~~
3. Out of the entire data set, what is the total amount of money
    people have paid in cash?
"""
with open("sales_data.txt", "r") as f:
    listArr = list(f)
    total = 0
    for line in listArr:
        arr = line.split('\t')
        payment = arr[2]
        amount = float(arr[3].strip("$\n"))
        if payment.lower() == "cash":
            total += amount
    # print("$" + str(round(total, 2)))
# Answer $123904942.34

"""
~~~~~~~~~~~~~~~~  Challenge 4  ~~~~~~~~~~~~~~~
4. What is the most popular payment type in Oakland in March?
"""
with open("sales_data.txt", "r") as f:
    listArr = list(f)
    payments = {}
    for line in listArr:
        # print(line)
        arr = line.split('\t')
        city = arr[0].lower()
        payment_type = arr[2].lower()
        if city == "oakland":
            if payment_type in payments.keys():
                payments[payment_type] += 1
            elif payment_type not in payments.keys():
                payments[payment_type] = 1
payments_types_key = max(payments, key=payments.get)
print(payments_types_key)
# Answer baseball cards

"""
~~~~~~~~~~~~~~~~  Challenge 5  ~~~~~~~~~~~~~~~
4. What is the most popular payment type in Oakland in March?
"""
