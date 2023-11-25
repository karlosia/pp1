current=int(input("Enter current product price: "))
previous=int(input("Enter previous product price: "))

if current<=8/10*previous:
    result=100-(current/previous*100)
    print(f"Buy the product!! Product price reduced by {result} %")
  