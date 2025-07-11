import pandas as pd  #import panda library
df = pd.read_csv("sample_product_data.csv")

# Q1. Load and Preview the Dataset

#read csv file
df = pd.read_csv("sample_product_data.csv")
#print csv file 
print(df)

#print first five rows
print(df.head())

#print information about columns and rows
print(df.info())

#print counts of rows and columns
print(df.shape)  


#Q2. Add a New Column: Total Revenue
# Add a column named "Revenue" = Price * Units_Sold   


#read csv file
df = pd.read_csv("sample_product_data.csv")
#creating a new column revenue 
df["Revenue"] = df["Price"] * df["Units_Sold"]
#print the table
print(df)  



#update DataFrame with new columns:
df.to_csv("updated_product_data.csv", index=False)
print(df)



#Q3. Sort Products by Revenue (High to Low) Code:

#sorting the revenue in descending order
top_revenue = df.sort_values("Revenue", ascending=False)
print(top_revenue)



#Q4. Show All Products In Stock

#we are checking the product is in Stock , where condition is true
in_stock_pdt = df[df["In_Stock"] == True]
#print the in_stock product
print(in_stock_pdt) 



#Q5. Average Revenue of Electronics Products

#making sure that category is electronics
elect = df[df["Category"] == "Electronics"]
#calculating average of revenue 
avg_mn = elect["Revenue"].mean() 
#print the average 
print("average mean is: " , avg_mn)  


 #Q6. Which Product Has the Highest Revenue?

#we will check the product which has max revenue
top_product = df.loc[df["Revenue"].idxmax()]
#print the product which has max revenue
print("Top Product by Revenue:\n", top_product)


#Q7. Products That Sold Over 300 Units and Are In Stock

#Combining two statements using AND(&) operator where
# we will check 2 conditions of Units_sold and In_stock
in_pdt = df[(df["Units_Sold"] > 300) & (df["In_Stock"] == True)]
#print the result
print(in_pdt)
