number=(input("Enter EAN-13 article number: "))

if len(number)==13:
    print("Number is correct")
    if number.startswith("590"):
        print("Article manufactured in POLAND")
else:
    print("Number is not correct") 


