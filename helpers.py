from distance import get_distance
from datetime import datetime, date


def sort_by_distance(data, lat, lon):
    list_without_far_away = []
    for restaurant in data:
        if get_distance(restaurant["location"][1], restaurant["location"][0], lat, lon) < 1.5:
            list_without_far_away.append(restaurant)
    
    list_with_distance = sorted(list_without_far_away, key=lambda k: get_distance(k["location"][1], k["location"][0], lat, lon))
    
    newList = sorted(list_with_distance, key=lambda k: k["online"], reverse=True)

    return newList




def sort_by_popularity(data):
    newList = sorted(data, key=lambda k: k["popularity"], reverse=True)
    if len(newList) > 10:
        return newList[:10]
    else:
        return newList

def d_months(date1, date2):
    return (date1.year - date2.year) * 12 + date1.month - date2.month   

def sort_by_date(data):
    # first we filter out all older than 4 months
    date_format = '%Y-%m-%d'
    today = date.today()

    filtered = filter(lambda restaurant: d_months(today, datetime.strptime(restaurant['launch_date'], date_format)) < 4, data)
    
    sorted_list = sorted(filtered, key=lambda restaurant: restaurant['launch_date'], reverse=True)

    if len(sorted_list) > 10:
        return sorted_list[:10]
    else:
        return sorted_list