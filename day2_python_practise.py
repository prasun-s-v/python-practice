"""Q1: Store Sales Totals by Category(You’re given a list of sales transactions.
Each item is a list: [category, amount].
Return a dictionary showing total sales for each category.)

LOGIC:"""
sales = [["electronics", 1500],["clothing", 500],["electronics", 1200],["grocery", 300],["clothing", 800]]
total_sales = {} #every sales total will be stored in it.
for category,amount in sales:
    #loop through the items, unpacking cat and amt
    if category in total_sales:
        #check if category in mapped in total_sales
        total_sales[category] += amount 
        # if it is mapped then add amount in existing total
    else:
        total_sales[category] = amount
        #if it is not mapped, then create a new cat which is equal to amount
print(total_sales)
#print total_sales based on cat and amount


"""Q2:Return Items with Price > ₹500
items = {"Fan": 900, "Book": 150, "AC": 35000, "Bottle": 90, "T-shirt": 600}
➡️ Expected Output: ["Fan", "AC", "T-shirt"]



logic:"""
ites = {"Fan": 900, "Book": 150, "AC": 35000, "Bottle": 90, "T-shirt": 600}
##using dictinary with loops
expen_item = [] #will collect all expensive item key-value

for key,value in ites.items():
    #loop each item with key-value
    if value > 500:
        #check if value is greater than 500
        expen_item += [key]
        # value matches and key will be stored to expen_item.
print(expen_item) #print expen_item

#********Using list comprehension*******
expen_item = [key for key,value in ites.items() if value>500 ]
#create a list comprehension which will take key as index
# then use for loop with key, value and 
#check whether the value is greater than 500
# if it matches the condition then print expen_items.
print(expen_item)


"""Q3: Build Price After Discount Dict(products = {"TV": 20000, "Microwave": 8000, "Fridge": 32000}
discount = 0.1
➡️ Expected Output:

python
Copy
Edit
{
  "TV": 18000.0,
  "Microwave": 7200.0,
  "Fridge": 28800.0
})

#logic:"""
def apply_discount(products,discount):
    #initialise empty dict to store discounted price
    discnted = {}
    #loop over items with name and price
    for name,price in products.items():
        #cal new_price after applying discount
        new_price = price * (1 - discount)
        #add the product and new_price into dictionary
        discnted[name] = new_price
    #return dictionary with discount
    return discnted
products = {"TV": 20000, "Microwave": 8000, "Fridge": 32000}
discount = 0.1
#print the product with applied discount
print(apply_discount(products,discount))


#Q4. Filter Product Names > 6 Characters (List Comprehension)
#products = ["Fridge", "TV", "WashingMachine", "Oven", "AC", "BluetoothSpeaker"]
#➡️ Expected Output: ["WashingMachine", "BluetoothSpeaker"]


#logic:

products = ["Fridge", "TV", "WashingMachine", "Oven", "AC", "BluetoothSpeaker"]
# pdt for pdt condition iterate over each product item 
# and len function check the length of products and if the condition met, product is added to cat list.

cat = [product for product in products if len(product) > 6  ]
#print the result
print(cat)






