from datetime import datetime, timedelta, date

def my_datetime(DateTime):
    return DateTime.strftime("%Y %m %d %H %M %S")

def saturdays():
    list_of_saturdays = []
    
    start_date = date(datetime.now().year, datetime.now().month, datetime.now().day)
    end_date = date(start_date.year + 1, 1, 1)

    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() == 5:
            print(current_date)
            list_of_saturdays.append(current_date)
        current_date += timedelta(days=1)
    
    return list_of_saturdays

def first_or_fifteenth(DateTime):
    if DateTime.day == 11 or DateTime.day == 15:
        return True
    else:
        return False
