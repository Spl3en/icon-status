import requests
import certifi
import json

def get_status (server):
    path = certifi.where()
    url = server + "/api/v1/status/peer/"
    r = requests.get(url, verify=path)
    return json.loads(r.text)
