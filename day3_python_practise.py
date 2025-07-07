"""Q1:Format Product Names
You’re given messy product names. Clean them.
products = ["  Air Conditioner", "Fridge ", " tv", "WASHING MACHINE  "]

logic:"""

products = ["  Air Conditioner", "Fridge ", " tv", "WASHING MACHINE  "]
clean_data = []
for dirty in products:
    cleaned = dirty.strip().lower()
    clean_data.append(cleaned)
print(clean_data)


"""Q2:Create a Function to Clean Product Names
Turn Q1 into a reusable function.
def clean_product_names(product_list):
    # your code
✅ Sample Output:

print(clean_product_names(["  AC ", " FAN", "cooler  "]))
# ['ac', 'fan', 'cooler']

logic:"""

def clean_product_names(product_list):
    clean_data = []
    for dirty in product_list:
        cleaned = dirty.strip().lower()
        clean_data.append(cleaned)
   #it prints the list inside the function and then prints None because the function doesn't return anything.
   #print(clean_data)
    return clean_data
#products = ["  Air Conditioner", "Fridge ", " tv", "WASHING MACHINE  "]
print(clean_product_names(["  AC ", " FAN", "cooler  "]))

"""Q3:Create a Summary Message for Each Product
products = ["Fan", "AC", "TV"]
prices = [1200, 25000, 15000]

logic:"""
products = ["Fan", "AC", "TV"]
prices = [1200, 25000, 15000]
# using range function to iterate all the product and prices, with len function.
for i in range(len(products)):
    #using i index which will iterate through all products and prices. and print the result
    print(f"{products[i]} is priced at RS{prices[i]}.")



"""Q4:Filter Invalid Product Codes
Valid product codes are alphanumeric only.
codes = ["TV123", "123AC", "!!Fan", "Cool#01", "Laptop"]

logic:"""
codes = ["TV123", "123AC", "!!Fan", "Cool#01", "Laptop"]
cod = []
for i in range(len(codes)):
    #You're calling .isalnum() on the entire list codes, not on each individual string. You should call it on the current item in the loop, like codes[i].isalnum().
    if codes[i].isalnum():
        #You're appending the index i, but the question asks for the valid product codes, so you should append codes[i].
        cod.append(codes[i])
print(cod)


"""Q5. Advanced: Create Product Dictionary

names = ["AC", "TV", "Fridge"]
prices = [25000, 18000, 30000]

logic"""

names = ["AC", "TV", "Fridge"]
prices = [25000, 18000, 30000]
#using zip function
zipped = zip(names,prices)
print(dict(zipped))
 
 #use index-based loop
 
 #create a empty dictionary to store key-value data
product_dict = {}
#loop over items with help of name length index
for i in range(len(names)):
    #iterating both product[i] and prices[i] items and storing them in product_dict
    product_dict[names[i]] = prices[i]
#print the result
print(product_dict)