import datetime

def time():
    # Get the current local date and time
    current_date_time = datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
    return (current_date_time)

