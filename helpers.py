from distance import get_distance


def sort_by_distance(data, lat, lon):
    list_without_far_away = []
    for restaurant in data:
        if get_distance(restaurant["location"][1], restaurant["location"][0], lat, lon) < 1.5:
            list_without_far_away.append(restaurant)
    
    newList = sorted(list_without_far_away, key=lambda k: get_distance(k["location"][1], k["location"][0], lat, lon))
    for r in newList:
        print(get_distance(r["location"][1], r["location"][0], lat, lon))
    return newList