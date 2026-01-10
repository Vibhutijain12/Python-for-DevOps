## Ques: Remote Server Health Check - Write a script that: Pings a list of servers Reports which servers are UP or DOWN

import socket

servers = [
    ("google.com", 80),
    ("localhost", 22),
    ("example.com", 443)
]

def is_host_up(): 
    timeout = 3

    for host, port in servers:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        try:
         sock.connect((host, port))
         print(f"{host}:{port} is UP")
        except:
         print(f"{host}:{port} is DOWN")
        finally:
         sock.close()


is_host_up()
