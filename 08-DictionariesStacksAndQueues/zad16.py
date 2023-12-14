def hotel_list(hotels):
    return ", ".join(hotel["name"]for hotel in hotels)

def avg_price(hotels):
    total_price=sum(hotel["price"] for hotel in hotels)
    average_price=total_price/len(hotels)
    return round(average_price)


def compare_prices(Hotels_in_Krakow,hotels_in_Sopot):
    avg_price_krakow=avg_price(Hotels_in_Krakow)
    avg_price_sopot=avg_price(hotels_in_Sopot)

    print(f'Hotels in Krakow: {hotel_list(Hotels_in_Krakow)}')
    print(f'Average hotel price in Krakow: {avg_price_krakow}\n')

    print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
    print(f"Average hotel price in Sopot: ${avg_price_sopot}\n")

    if avg_price_krakow < avg_price_sopot:
        print("Cheaper hotels in: Krakow")
    elif avg_price_sopot < avg_price_krakow:
        print("Cheaper hotels in: Sopot")
    else:
        print("Average prices are the same in Krakow and Sopot")








Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

compare_prices(Hotels_in_Krakow,hotels_in_Sopot)