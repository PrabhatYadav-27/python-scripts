# This script is used to check the server is reachable or not

import os

def server_check(host):
    # use -n for windows or -c for linux/mac
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is not reachable")
    
# calling the function
server_check("8.8.8.8")