from flask import Flask, request
import requests
import json
from distance import get_distance

app = Flask(__name__)

@app.route('/discovery')
def api():
    # getting the user data
    lat_user  = float(request.args.get('lat', None))
    lon_user  = float(request.args.get('lon', None))
    
    
    temp = requests.get("https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json")
    print(get_distance(lat_user, lon_user, 60.156621, 24.935637))
    return json.loads(temp.content)

if __name__ == '__main__':
    app.run(port=5000, debug=True)