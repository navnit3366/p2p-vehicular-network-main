# The server - to enable communication between clients (or vehicles in this case)

# miscellaneous functions in various files
# from ip_port_gen import *
# from sos import *

# networking packages
import threading
import socket

'''
============
SOS Handling
============
'''
sos_msg = [
    "ACCIDENT",
    "MALFUNCTION",
    "LOW_FUEL",  
    "HELP",
]

responders = []
responders_address = []

def check_sos(msg):
    if msg in sos_msg:
        alert = "SOS Alert! Car facing with "+msg+". Please respond!"
        msg_broadcast(responders, alert)
        return 1
    else:    
        return 0

def add_sos_responder(client, address):
    while True:
        client.send("Are you a SOS responder ? (Y/N)".encode("ascii"))
        isSOS = client.recv(2048).decode("ascii")
        if isSOS == 'Y': 
            responders.append(client)
            responders_address.append(address)
            client.send("You are now a SOS Responder. Whenever a SOS is broadcast, you will get a message!".encode("ascii"))
            print("SOS Responder added. ",end='')
            return 1
        elif isSOS == 'N':
            return 0
        else:
            client.send("Invalid response, please try again!".encode("ascii"))


'''
======================================================
Initialise server and bind it with IP Address and Port
======================================================
'''
# we need to define these for the clients to know where to connect to
host = '127.0.0.1'                          #localhost address
port = 11111
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()  
clients = []
client_address = []
nicknames = []

''' 
================================================
Function to broadcast message
(*)to vehicles       - for coordination related
(*)to SOS responders - for emergency
================================================
'''
def msg_broadcast(receivers, msg):
    for node in receivers:
        node.send(msg.encode("ascii"))

'''
========================================================
Function to handle messages sent from different vehicles
========================================================
'''
def msg_process(client):
    while True:
        # Try to recieve input from a client
        try:
            msg = client.recv(2048).decode("ascii")
            response = check_sos(msg)
            if response:
                print("\n----------------------------------------------")
                print("*** Client SOS distress signal. Responders alerted! ***")
                print("\n----------------------------------------------")
            else:
                msg_broadcast(clients, msg)
        # If cannot, remove it from the network
        except:
            clients.remove(client)
            client.close()
            print("Connection to client stopped due to disconnection!")
            break

'''
==========================
New Client adding function
==========================
'''
def receive_new_client():
    while True:
        client, address = server.accept()
        # check if client is a SOS responder or just a normal client
        response = add_sos_responder(client, address)
        if not response:
            clients.append(client)
            client_address.append(address)

        # print to server console if connection with a client is successful
        print("Connection established successfully with "+str(address))
        client.send("Connection with the server successful".encode("ascii"))

        server_thread = threading.Thread(target=msg_process, args=(client,))
        server_thread.start() 

print("Server is listening to incoming connection requests. Currently on standby!")
receive_new_client()

# def main():
#     print("Server has started listening .....")
#     receive_new_client()

# if __name__ == "__main__":
#     main()

