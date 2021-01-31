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
    
    temp = requests.get("https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json")
    restaurants = json.loads(temp.content)["restaurants"]

    print(sort_by_popularity(sort_by_distance(restaurants, lat_user, lon_user)))
    return {"hej":sort_by_date(sort_by_distance(restaurants, lat_user, lon_user))}

if __name__ == '__main__':
    app.run(port=5000, debug=True)