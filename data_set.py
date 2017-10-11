"""Data scraping using Python String Methods."""
"""
Questions for today’s File I/O problem:

3. Out of the entire data set, what is the total amount of money
    people have paid in cash?
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
    data_array = []
    data_dictionary = {}
    for word in f.readline().split('\t'):
        data_array.append(word.strip('$\n'))
        # iterate thru the array
        # if array[0] !in dictionary, create a new key with value 
    print(data_array)
