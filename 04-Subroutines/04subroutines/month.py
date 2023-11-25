#define a function month(n) that returns a month name 
#based on the month number (values from 1 to 12).

def get_month_name(month_number):
    months = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]

    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return 'Invalid month number'





         