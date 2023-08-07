# useful packages for logic
import random
import math

# networking packages
import socket

# host IP and port handling functions
def host_gen():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_ip

def port_gen():
    host_port = random.randint(10000,99999)
    return host_port

def print_device_details(host, port):
    print("Current device location is: ", end='')
    print(str(host)+":"+str(port))
    return

if __name__ == "__main__":
    host = host_gen()
    port = port_gen()
    print_device_details(host, port)