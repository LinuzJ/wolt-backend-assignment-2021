from flask import Flask, request
import requests
import json
from distance import get_distance
from helpers import sort_by_distance, sort_by_popularity, sort_by_date

app = Flask(__name__)

@app.route('/discovery')
def api():
    # getting the user data
    lat_user  = float(request.args.get('lat', None))
    lon_user  = float(request.args.get('lon', None))
    
    restaurant_data = requests.get("https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json")
    restaurants = json.loads(restaurant_data.content)["restaurants"]

    sorted_restaurants = sort_by_distance(restaurants, lat_user, lon_user)
    
    return_data = {
        "sections": [
            {
                "title": "Popular Restaurants",
                "restaurants": sort_by_popularity(sorted_restaurants)[:10]
            },
            {
                "title": "New Restaurants",
                "restaurants": sort_by_date(sorted_restaurants)[:10]
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