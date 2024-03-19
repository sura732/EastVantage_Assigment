import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite.connect('Company.db')

#extract the total quantities of each item bought per customer aged 18-35.
#For each customer, get the sum of each item
#Items with no purchase (total quantity=0) should be omitted from the final list
#No decimal points allowed (The company doesn’t sell half of an item )

sql_query = """
SELECT c.Customer_id, c.Age, i.Item_name, SUM(CAST(o.Quantity AS INTEGER)) AS Total_Quantity
FROM Customer c
JOIN Sales s ON c.Customer_id = s.Customer_id
JOIN Orders o ON s.Sales_id = o.Sales_id
JOIN Items i ON o.Item_id = i.Item_id
WHERE c.Age BETWEEN 18 AND 35
GROUP BY c.Customer_id, i.Item_name
HAVING SUM(CAST(o.Quantity AS INTEGER)) > 0;
"""

# Execute the SQL query and read into pandas dataframe
df = pd.read_sql_query(sql_query, conn)

# Store the results in a CSV file using semicolon as delimiter
df.to_csv('output_file.csv', index=False, sep=';', columns=['Customer_id', 'Age', 'Item_name', 'Total_Quantity'])

# Close the database connection
conn.close()
