class Product:
    
    def __init__(self, id, description, price = 0):
        self.id = id
        self.description = description
        self.price = price

class ProductsService:
    products = [
        Product(101, "Coke Can", 25.00),
        Product(208, "Lays Chips", 105.00),
        Product(560, "Mott's Apple Juice", 200.00)
    ]
    
    @classmethod
    def get_products(cls):
        return cls.products
    
    @classmethod
    def find(cls, id):
        for product in cls.products:
            if id == product.id:
                return product
        
        return None