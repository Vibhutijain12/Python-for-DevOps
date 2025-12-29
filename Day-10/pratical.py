import requests
import json 

response = requests.get("https://dummyjson.com/todos")
data = response.json()
# print(data)

for todo in data["todos"]:  ## Looping through each todo item
    # print(todo)
    for key, value in todo.items():
        print(f"{key}: {value}")
    print("-----")

if data["todos"]: 
    print(data["todos"][0].get("todo"))

#### Example-2: 

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

print(type(server_config))

def get_server_config():
        server_name =  input("Enter server name (server1, server2, server3):")
        return server_config.get(server_name, {}).get("status", "unknown")

status = get_server_config()
print(f"Status of server: {status}")


