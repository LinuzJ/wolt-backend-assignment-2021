from flask import Flask, request
import requests
import json
from helpers import sort_by_distance, sort_by_popularity, sort_by_date, get_distance

app = Flask(__name__)

@app.route('/discovery')
def api():
    
    # getting the user data
    lat_user  = float(request.args.get('lat', None))
    lon_user  = float(request.args.get('lon', None))
    
    # getting the restaurant data from the source
    restaurant_data = requests.get("https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json")
    restaurants = json.loads(restaurant_data.content)["restaurants"]

    # filtering out restaurants that are too far away and sorting them by distance
    sorted_restaurants = sort_by_distance(restaurants, lat_user, lon_user)

    # building the return structure
    return_data = {
        "sections": [
            {
                "title": "Popular Restaurants",
                "restaurants": sort_by_popularity(sorted_restaurants)
            },
            {
                "title": "New Restaurants",
                "restaurants": sort_by_date(sorted_restaurants)
            },
            {
                "title": "Nearby Restaurants",
                "restaurants": sorted_restaurants[:10]
            }

        ]
    }

    return return_data

if __name__ == '__main__':
    app.run(port=5000, debug=True)