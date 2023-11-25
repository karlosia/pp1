def convert_to_12_hour_format(hour, minute):
    period="am"
    if hour>=12:
        period="pm"
    if hour>12:
        hour=hour-12
    return hour, minute, period

def main():
    try:
        time=(input("Enter time (24-hour format: HH:MM ): "))
        hour, minute=map(int, time.split(':'))
        if 0<=hour<=23 and 0<=minute<=59:
            hour_12, minute, period= convert_to_12_hour_format(hour,minute)
            print(f"Time in 12-hour format: {hour_12}:{minute:02d} {period}")
        else:
            print("Invalid input. Please enter a valid time.")    
    except ValueError:
        print("Invalid input. Please enter a valid time in HH:MM format.")

if __name__=="__main__":
    main()        
