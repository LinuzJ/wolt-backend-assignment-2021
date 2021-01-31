import math

def get_distance(lat_1, lng_1, lat_2, lng_2): 
    d_lat = math.radians(lat_2) - math.radians(lat_1)
    d_lng = math.radians(lng_2) - math.radians(lng_1) 

    temp = (  
         math.sin(d_lat / 2) ** 2 
       + math.cos(lat_1) 
       * math.cos(lat_2) 
       * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))