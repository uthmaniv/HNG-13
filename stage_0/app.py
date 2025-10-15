from flask import Flask, Response
import requests
from datetime import datetime
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def get_profile():
    try:
        response = requests.get('https://catfact.ninja/fact', timeout=5)
        response.raise_for_status()  
        cat_fact = response.json().get('fact', 'No cat fact available.')
    except requests.RequestException:
        cat_fact = "Could not fetch cat fact at this time."

    data = OrderedDict([
        ("status", "success"),
        ("user", {
            "email": "uthmanyahaya@gmail.com",
            "name": "Usman Yahaya",
            "stack": "Python/Flask"
        }),
        ("timestamp", datetime.utcnow().isoformat() + "Z"),
        ("fact", cat_fact)
    ])

    return Response(json.dumps(data), mimetype='application/json'), 200

if __name__ == '__main__':
    app.run(debug=True)
