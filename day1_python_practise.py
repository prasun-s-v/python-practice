#Q1: Even or Odd (Write a function that accepts a number and returns whether it’s even or odd)
# My logic: Tried to use if-else but had confusion with % operator and syntax.
# Learned: Use == for comparison. Now I understand even vs odd condition.
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#Q2: Calculate total revenue using a for loop (prices = [100, 299, 120, 85, 450])
#My logic: Tried to use loop over items, but i was stuck on the initialise condition.
#Learned: how to initialise loop conditions.   
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.

prices = [100, 299, 120, 85, 450]
total = 0
for x in prices:
	total += x
print(total)

#Q3. Categorize Product by Price (Create a function that takes a price and returns)
#My logic : USe of if-elif and else conditions.
#Learned : use of if-elif and else conditions.
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.
def prc_return(price):
    if price < 100:
        print("Budget")
    elif price >100 and price < 300 :
        print("Mid-range")
    else:
        print("Premium")
prc_return(price = int(input("enter price: ")))

#Q4. Find Maximum from List (Without max()  prices = [120, 340, 50, 999, 432])
#My logic: use of loop over items
#Learned : use of loop over item with the help of slicing.
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.

price = [120, 340, 50, 999, 432]
max_price =price[0]
for i in price[1:]:
    if i > max_price:
        max_price = i
print("Maximum price:", max_price)

#Q5. Create a Simple Discount Function (Write a function to apply a 10% discount and return the new price.)
#my logic: I was not able to think anything, i was thinking of using if- else with built in function. But my approach was not correct.
#Learned: use of round built-in function to  get result with 2 decimal number.
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.
def ten_per(price):
    #two approaches i have tried.
    """disc_price = price * 0.90
    return disc_price """
    return round(price*0.90, 2)
print(ten_per(price = int(input("enter price: "))))

#Q6. From a list of product names, print only those with more than 6 letters.( products = ["Shirt", "Television", "Fan", "Refrigerator", "Book"])
#my logic: To use loop over items.
#learned: to use len function.
# Note: This code was written with AI assistance while learning.
# I focused on understanding and rewriting the logic for each question.

products = ["shirts", "Television", "Fan", "Refrigerator", "Book"]
for product in products:
    if len(product) > 6:
        print(product)




