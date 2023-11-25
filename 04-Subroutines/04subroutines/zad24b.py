from zad24 import is_in_range

def main():
    number=int(input("Enter a number: "))
    range_start=int(input("Enter range start: "))
    range_end=int(input("Enter range end: "))

    result=is_in_range(number,range_start,range_end)
    
    print(f"Number {number} in the range <{range_start},{range_end}>: {result}")

if __name__ == "__main__":
    main()        


