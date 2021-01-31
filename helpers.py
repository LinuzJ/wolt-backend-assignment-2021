from datetime import datetime, date
import math

# filtering out restaurants that are too far away and sorting them by distance
def sort_by_distance(data, lat, lon):
    
    # Start by filtering out all restaurants further away than 1,5km
    filtered = filter(lambda restaurant: get_distance(restaurant["location"][1], restaurant["location"][0], lat, lon) < 1.5, data)
    
    # Then we sort them by distance
    list_with_distance = sorted(filtered, key=lambda k: get_distance(k["location"][1], k["location"][0], lat, lon))
    
    # Finally we sort them by their status
    newList = sorted(list_with_distance, key=lambda k: k["online"], reverse=True)

    return newList



# Sort by popularity and return 10 or less
def sort_by_popularity(data):
    newList = sorted(data, key=lambda k: k["popularity"], reverse=True)
    
    if len(newList) > 10:
        return newList[:10]
    else:
        return newList

# Helper function for sort_by_date
def d_months(date1, date2):
    return (date1.year - date2.year) * 12 + date1.month - date2.month   

# Sort by date and return 10 or less
def sort_by_date(data):
    
    # First we filter out all older than 4 months
    date_format = '%Y-%m-%d'
    
    today = date.today()
    # Filter away everything older than 4 months
    filtered = filter(lambda restaurant: d_months(today, datetime.strptime(restaurant['launch_date'], date_format)) < 4, data)
    # Sort by date
    sorted_list = sorted(filtered, key=lambda restaurant: restaurant['launch_date'], reverse=True)

    if len(sorted_list) > 10:
        return sorted_list[:10]
    else:
        return sorted_list


# Returns distance between two coordinates in km
def get_distance(lat_1, lng_1, lat_2, lng_2): 
    
    d_lat = math.radians(lat_2) - math.radians(lat_1)
    d_lng = math.radians(lng_2) - math.radians(lng_1) 

    calculation = (  
         math.sin(d_lat / 2) ** 2 
       + math.cos(lat_1) 
       * math.cos(lat_2) 
       * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(calculation), math.sqrt(1 - calculation)))