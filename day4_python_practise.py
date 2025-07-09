"""Q1. Filter All TVs from Sales List

sales = [
    {"product": "TV", "price": 15000},
    {"product": "AC", "price": 25000},
    {"product": "TV", "price": 18000}
]
✅ Output:

[{"product": "TV", "price": 15000}, {"product": "TV", "price": 18000}]"""

#code:

sales = [
    {"product": "TV", "price": 15000},
    {"product": "AC", "price": 25000},
    {"product": "TV", "price": 18000}
]
#iterating each items in sales list
for items in sales:
    #filter if product item = Tv then condition matches
    if items["product"] == "TV":
        #print the items matched with condition
        print(items)

"""Q2. Total Sales for Each Product
✅ Output:

{'TV': 33000, 'AC': 25000}"""

#code:

sales = [
    {"product": "TV", "price": 15000},
    {"product": "AC", "price": 25000},
    {"product": "TV", "price": 18000}
]
#initialise an empty dictionary
totals = {}
#iterating each items in sales list
for items in sales:
    #extracting product item for each transaction
    product = items["product"]
    #extracting item price for each transaction
    price = items["price"]
    #check if product in totals
    if product in totals:
        #condt met then totals product will be added to existing price
        totals[product] += price
    else:
        #if not, create a new entry where product is key and price is value.
        totals[product] = price
#print the total entries
print(totals)

"""Q3.Create Summary Message for Each Transaction
✅ Output:

TV was sold for ₹15000
AC was sold for ₹25000
TV was sold for ₹18000 """

#code:

sales = [
    {"product": "TV", "price": 15000},
    {"product": "AC", "price": 25000},
    {"product": "TV", "price": 18000}
]

#iterating each items in sales list
for item in sales:
    #we should use dixtionary keys to access the value, not index.
    print(f"{item['product']} was sold for Rs{item['price']}.")

"""Q4. Return Only Products > ₹20000
✅ Output:

[{"product": "AC", "price": 25000}, {"product": "TV", "price": 22000}] """

#code:
sales = [
    {"product": "TV", "price": 15000},
    {"product": "AC", "price": 25000},
    {"product": "TV", "price": 18000},
    {"product": "TV", "price": 22000}
]
#initialize an empty list, to store products that meet the price conditions.
totals = []
#iterating each items in sales list
for i in sales:
# check condt if price of current item is > 20000
    if i['price'] > 20000:
#if condt met, then append the item to totals list.
        totals.append(i)
#print total list
print(totals)




