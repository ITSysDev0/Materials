import products

# assuming that the user will enter a valid input
id = int(input("Enter a product ID: "))

try:
    product = products.ProductsService.find(id)
    
    print("Description:", product.description)
    print("Price:", product.price)
except LookupError as e:
    print(e)