"""✅ Q1. Create a DataFrame manually
Create a DataFrame with columns: "Product", "Price", "Category"
Add at least 5 rows manually.

Code:"""

import pandas as pd #import library
#creating data dictionary
data = { 'Product' : ['Laptop', 'Phone', 'Tablet', 'TV', 'Watch'], 'Price' : [50000, 20000, 15000, 40000, 8000], 'Category' :['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Wearable']
}


#creating dataframe(table) with help of pandas(pd)
df = pd.DataFrame(data)

#print the table
print(df)



"""✅ Q2. Filter Products
Print only products whose price is more than ₹20,000.

Code:"""

import pandas as pd #import library
#creating data dictionary
data = { 'Product' : ['Laptop', 'Phone', 'Tablet', 'TV', 'Watch'], 'Price' : [50000, 20000, 15000, 40000, 8000], 'Category' :['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Wearable']
}


#creating dataframe(table) with help of pandas(pd)
df = pd.DataFrame(data)

#print the sorted table base on product price
print(df[df['Price']  > 20000])

"""✅ Q3. Add a new column
Add a column "Discounted_Price" = Price – 10% of price.


Code:"""

import pandas as pd #import library
#creating data dictionary
data = { 'Product' : ['Laptop', 'Phone', 'Tablet', 'TV', 'Watch'], 'Price' : [50000, 20000, 15000, 40000, 8000], 'Category' :['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Wearable']
}

#creating dataframe(table) with help of pandas(pd)
df = pd.DataFrame(data)

#add new coulmn for discounted_price 
#discount is 0f 10% on price
df['Discounted_Price'] = df['Price'] - (df['Price'] * 0.10)

print(df)

"""✅ Q4. Sort by Price
Sort the DataFrame in descending order of "Price".

code:"""
import pandas as pd #import library
#creating data dictionary
data = { 'Product' : ['Laptop', 'Phone', 'Tablet', 'TV', 'Watch'], 'Price' : [50000, 20000, 15000, 40000, 8000], 'Category' :['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Wearable']
}

#creating dataframe(table) with help of pandas(pd)
df = pd.DataFrame(data)

#sort the value in descending order
#using condition "ascending = False" to get desc order
print(df.sort_values('Price',ascending = False))


"""✅ Q5. Summary Report
Print the average price of products in the "Electronics" category.

Code:"""

import pandas as pd #import library
#creating data dictionary
data = { 'Product' : ['Laptop', 'Phone', 'Tablet', 'TV', 'Watch'], 'Price' : [50000, 20000, 15000, 40000, 8000], 'Category' :['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Wearable']
}

#creating dataframe(table) with help of pandas(pd)
df = pd.DataFrame(data)

#filter only electronics row
elect_prodt = df[df['Category'] == 'Electronics']
#find out the mean(avg) price of electronics
avg_price = elect_prodt['Price'].mean()

#print the avg price 
print("Average price of electronics: " , avg_price)

