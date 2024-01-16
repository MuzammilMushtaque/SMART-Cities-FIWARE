
# Extract the Outcomes of parking-manager from Fiware/Orion and Display in local host


# app.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

context_broker_url = 'http://host.docker.internal:1026'

latest_parking_status = {}

@app.route('/')
def index():
    # Get real-time parking data from Context Broker
    parking_data = get_parking_data()

    # Update global variable with latest parking status
    global latest_parking_status
    latest_parking_status = parking_data
    return render_template('index.html', parking_data=parking_data)

def get_parking_data():
    response = requests.get(f'{context_broker_url}/v2/entities?type=ParkingSpot')
    
    if response.status_code == 200:
        entities = response.json()
        parking_data = {}

        for entity in entities:
            spot_id = entity['id']
            status = entity.get('status', {}).get('value', 'Unknown')
            timestamp = entity.get('status', {}).get('metadata', {}).get('timestamp', {}).get('value', 'Unknown')
            parking_data[spot_id] = {'status': status, 'timestamp': timestamp}


        return parking_data
    else:
        return {}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')