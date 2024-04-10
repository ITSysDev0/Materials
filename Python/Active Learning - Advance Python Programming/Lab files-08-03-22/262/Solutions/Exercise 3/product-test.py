from products import Product
from products import ProductsService

p1 = Product(101, "Coke Can", 25.00)
p2 = Product(208, "Lays Chips", 105.00)
p3 = Product(560, "Mott's Apple Juice", 200.00)

products = [p1, p2, p3]

for p in products:
    print("ID:", p.id)
    print("Description:", p.description)
    print("Price:", p.price)
    print()

products = ProductsService.__products