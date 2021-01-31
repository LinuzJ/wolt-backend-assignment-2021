from flask import Flask
import requests
import json
from distance import get_distance

app = Flask(__name__)

@app.route('/')
def api():
    temp = requests.get("https://raw.githubusercontent.com/woltapp/summer2021-internship/main/restaurants.json")
    print(get_distance(60.171987, 24.941244, 60.156621, 24.935637))
    return json.loads(temp.content)

if __name__ == '__main__':
    app.run(port=5000, debug=True)