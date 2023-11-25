number_of_products=int(input("Enter the number of products purchased: "))
product_price=int(input("Enter the product price: "))

if number_of_products>2:
    pay=2*product_price+0.75*(number_of_products-2)*product_price
    print(f"Number of products purchased: {number_of_products}. Product price: {product_price}. Amount to pay: {pay}.")
else:
    pay=2*product_price
    print(f"Number of products purchased: {number_of_products}. Product price: {product_price}. Amount to pay: {pay}.")

