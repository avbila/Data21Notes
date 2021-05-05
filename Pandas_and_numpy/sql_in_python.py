import sqlalchemy
import pandas as pd
import numpy as np

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'
# or [Check which works]
# driver = 'ODBC+Driver+17+for+SQL+Server'

engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

connection = engine.connect()

result = engine.execute('SELECT * FROM Products')
print(result)

# # first way : one row at a time
# first_row = result.fetchone()
# print(first_row)
#
# # second way : get all rows
# all_rows = result.fetchall()
# print(all_rows)
#
# # third way : many
# many_rows = result.fetchmany(10)
# print(many_rows)
#
# # Getting column names:
# print(result.keys())

row = list(result)[0]
print(row)
# for x in row:
#     print(x)
#     print(type(x))
print(float(row[5]))

data = pd.read_sql('SELECT * FROM Products', connection, index_col='ProductID')
print(data)
for row in data:
    print(row)

