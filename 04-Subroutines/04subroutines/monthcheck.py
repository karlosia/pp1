from month import get_month_name


def main():
    month_number=7
    month_name=get_month_name(month_number) 
    print(f'The name of the {month_number}th month is: {month_name}')

if __name__ == "__main__":
    main()