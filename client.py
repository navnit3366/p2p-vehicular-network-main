# A client - A vehicle

# networking packages
import threading
import socket

signals = [
    "TA",   # TRAFFIC_AHEAD
    "BWA",  # BAD_WEATHER_AHEAD
    "RBA",  # ROAD_BLOCKAGE_AHEAD
    "LVA",  # LOW_VISIBILITY_AHEAD
    "DA"    # DIVERSION_AHEAD
]

'''
======================================================================
Code Section to initialise server and bind it with IP Address and Port
======================================================================
'''
server_ip = '127.0.0.1'
server_port = 11111
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip,server_port))

'''
===============================
Functions related to networking
===============================
'''
def receive_from_server():
    while True:
        try:
            msg = client.recv(2048).decode("ascii")
            print("NETWORK: "+msg)
        except:
            print("Oops! There was a hiccup while receiving signal from the server")
            client.close()
            exit()
            break

def msg_to_network():
    while True:
        msg = input("")
        client.send(msg.encode("ascii"))


'''
=========================================
Functions related to vehicle coordination
=========================================
'''

# Dummy function(s) as placeholders to show data from various sensors in vehicle
def report_generation():
    location_of_vehicle()
    weather_conditions_around()
    traffic_ahead()
    return

def location_of_vehicle():
    # Uses GPS sensor to get the location of this particular vehicle
    pass
    return

def weather_conditions_around():
    # uses sensors like humidity sensor, temperature sensor, light sensor  (for sunlight or cloudy weather)
    pass
    return

def traffic_ahead():
    # Use of DSRC protocol to communicate with nearby vehicles and get the traffic details
    pass
    return

# thread creation for this particular client for receiving and sending signals
print("Vehicle has started connection to the server .....")
this_client_thread = threading.Thread(target=receive_from_server)
this_client_thread.start()
this_client_thread = threading.Thread(target=msg_to_network)
this_client_thread.start()