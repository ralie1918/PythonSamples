import pandas as pd
import mysql.connector

# Setup MySQL connection
db = mysql.connector.connect(
    host="<IP>",              # your host, usually localhost
    user="<USER>",            # your username
    password="<PASS>",        # your password
    database="<DATABASE>"     # name of the data base
)   

# You must create a Cursor object. It will let you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM <TABLE>")

# Put it all to a data frame
sql_data = pd.DataFrame(cur.fetchall())
sql_data.columns = cur.column_names

# Close the session
db.close()

# Show the data
print(sql_data.head())