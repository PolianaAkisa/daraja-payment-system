from datetime import datetime

def get_timestamp():

    #print(datetime.datetime.now())

    unformatted_time= datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    #print(formatted_time,"this is the formatted time")
    
    return formatted_time