from products import ProductsService

products = ProductsService.get_products()

for product in products:
    print("ID:", product.id)
    print("Description:", product.description)
    print("Price:", product.price)
    print()

# assuming that the user will enter a valid input
id = int(input("Enter a product ID: "))
product = ProductsService.find(id)

if product is not None:
    print("Description:", product.description)
    print("Price:", product.price)
else:
    print("That product doesn't exist.")