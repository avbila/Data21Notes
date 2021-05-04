import sqlalchemy

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'ODBC+Driver+17+for+SQL+Server'

engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")
