import requests
import certifi
import json

def get_status (server):
    try:
        path = certifi.where()
        url = server + "/api/v1/status/peer/"
        r = requests.get(url, verify=path)
        return json.loads(r.text)
    except:
        return {
            'status' : 'offline : Endpoint unreachable',
            'consensus' : 'Unknown',
            'block_height' : 'Unknown',
            'total_tx' : 'Unknown',
            'unconfirmed_tx' : 'Unknown',
        }
