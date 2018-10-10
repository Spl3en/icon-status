import requests
import certifi
import json

def status (url):
    try:
        path = certifi.where()
        endpoint = url + "/api/v1/status/peer/"
        r = requests.get(endpoint, verify=path)
        result = json.loads(r.text)
        result['url'] = url
        return result
    except:
        return {
            'status' : 'offline : Endpoint unreachable',
            'consensus' : 'Unknown',
            'block_height' : 'Unknown',
            'total_tx' : 'Unknown',
            'unconfirmed_tx' : 'Unknown',
            'url' : url,
        }
