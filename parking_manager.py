''' 
Create a python application program that interact with the Context Broker
to manage the status of Parking Spots using NGSI-v2.
'''

import requests
import json
import random
import time
from datetime import datetime

# Replace 'context_broker_url' with your actual Context Broker URL
context_broker_url = 'http://host.docker.internal:1026'
entity_type = 'ParkingSpot'
num_parking_spots = 10

def create_data_model():
    for i in range(1, num_parking_spots + 1):
        entity = {
            'id': f'ParkingSpotid{i}',
            'type': entity_type,
            'status': {
                'type': 'Text',
                'value': 'Free',
                'metadata':{
                    'timestamp':{
                        'type':'DateTime',
                        'value': datetime.now().isoformat()
                        }
                    }
            }     
        }
        #print(f"Creating entity: {entity}")

        headers = {'Content-Type': 'application/json'}
        url = f'{context_broker_url}/v2/entities'
        response = requests.post(url, json=entity, headers=headers)

        if response.status_code == 201:
            print(f"Entity created successfully: {entity['id']}")
        else:
            print(f"Failed to create entity {entity['id']}. Status Code: {response.status_code}")
            print(f"Response content: {response.content}")



def update_parking_status():
    aa = True
    while aa == True:   # Last long to 100 times Update
        spot_to_update = random.choice(range(1, num_parking_spots + 1))
        new_status = 'Occupied' if random.choice([True, False]) else 'Free'

        entity_id = f'ParkingSpotid{spot_to_update}'
        metadata = {'time_stamp': {'value': datetime.now().isoformat()}}
        data = {'status': {'value': new_status, 'metadata': metadata}}
        # print(f"Updating entity ID: {entity_id}")
        # print(f"Update data: {json.dumps(data)}")

        headers = {'Content-Type': 'application/json'}
        url = f'{context_broker_url}/v2/entities/{entity_id}/attrs'
        response = requests.patch(url, json=data, headers=headers)

        if response.status_code == 204:
            print(f"Parking spot {spot_to_update} updated: {new_status}, at time {data['status']['metadata']['time_stamp']['value']}")
        else:
            print(f"Failed to update parking spot {spot_to_update}. Status Code: {response.status_code}")
            print(f"Response content: {response.content}")

        time.sleep(5)  # Update every 5 seconds
        aa = True




if __name__ == '__main__':
    create_data_model()
    time.sleep(5)  # Wait for 5 seconds to allow entities to be created
    update_parking_status()


