# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vibhutijain9812.atlassian.net/rest/api/3/project"

API_TOKEN = " "

auth = HTTPBasicAuth("vibhutijain9812@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# output = (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
print(output) 

for project in output:   ## Iterate through each project in the output
    # # print(project) 
    for key, value in project.items():   ## Iterate through each key-value pair in the project dictionary
        print(f"{key}: {value}")   ## Print the key and its corresponding value
    print("------")   ## Print a newline for better readability between projects


# if project:                  ## last project in the list
#     data = (project.get('id'))
#     print(f"Project ID: {data}")


    if 'id' and 'name' in project:
        project_id = project['id']
        project_name = project['name']
        print(f"Project ID: {project_id}")
        print(f"Project Name: {project_name}")
    print("======")   ## Print a separator between different projects

