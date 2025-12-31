from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    
    url = "https://vibhutijain9812.atlassian.net/rest/api/3/issue/bulk"


    API_TOKEN = " " 
    auth = HTTPBasicAuth("vibhutijain9812@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({
        "issueUpdates": [
        {
        "fields": {
            "issuetype": {
            "id": "10023"
            },
            "project": {
            "key": "DT"
            },
            "summary": "First Ticket",
            "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                "type": "paragraph",
                "content": [
                    {
                    "type": "text",
                    "text": "The order placed on 5th June is still in pending status. Please resolve this issue urgently."
                    }
                ]
                }
            ]
            }
        },
        "update": {}
        }
    ]
    })


    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
