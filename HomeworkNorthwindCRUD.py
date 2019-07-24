from PythonODBC import Northwind


table = 'Products'

my_db = Northwind()
rows = my_db.read_from_db('Products')
for row in rows:
    print(row.ProductName)
