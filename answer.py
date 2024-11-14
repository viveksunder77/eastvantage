import sqlite3 
import pandas as pd 


conn  = sqlite3.connect('S30 ETL Assignment.db')

customers_df = pd.read_sql_query('select * from customers where age between 18 and 35',conn)
# print(customers_df)
orders_df  = pd.read_sql_query('select * from orders where quantity > 0',conn)
sales_df = pd.read_sql_query('select * from sales',conn)
items_df = pd.read_sql_query('select * from items',conn)

final_df = customers_df.merge(sales_df,on='customer_id')\
            .merge(orders_df,on='sales_id')\
            .merge(items_df,on= 'item_id')

result_df = final_df.groupby(['customer_id','age','item_name']).sum('quantity').reset_index()

# print(result_df[['customer_id', 'age', 'item_name', 'quantity']])

result_df.to_csv('output.csv', sep=';', index=False)


