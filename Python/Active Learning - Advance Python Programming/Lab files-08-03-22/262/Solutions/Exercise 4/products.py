class ProductNotFoundException(BaseException):
    def __init__(self, message="That product doesn't exist."):
        self.message = message
        super(ProductNotFoundException, self).__init__(self.message)

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
    def find(cls, id):
        output = None
        for product in cls.products:
            if id == product.id:
                output = product
        if output == None:
            raise LookupError("That product doesn't exist.")
        else:
            return output