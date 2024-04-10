# copied from products.py
class Product:
    
    def __init__(self, id, description, price = 0):
        self.id = id
        self.description = description
        self.price = price
    
    def __str__(self):
        output = ""
        output = output + "ID: " + str(self.id) + "\n"
        output = output + "Description: " + str(self.description) + "\n"
        output = output + "Price: " + str(self.price) + "\n"
        
        return output

# copied from products.py
class ProductsService:
    __products = [
        Product(101, "Coke Can", 25.00),
        Product(208, "Lays Chips", 105.00),
        Product(560, "Mott's Apple Juice", 200.00)
    ]