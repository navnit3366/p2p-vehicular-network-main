Note, Python is a prerequisite for the system that is going to run the script(s). To install
python, follow the instruction after downloading the setup from -
https://www.python.org/downloads/release/python-3102/

This brief tutorial will help the user simulate the server and client(s) on the same
computer using different instances of the terminal posing as different clients (some
being vehicles, some being pedestrians, some being SOS responders).

Please note, do create atleast 3 instances of client who is not a SOS responder and atleast 2
instances of client who is a SOS responder in order to clearly see the communication between
vehicles, SOS responders and the server.

Step 1: 

Extract the .zip file provided. This zip file, when extracted, shall result in a
folder containing the following files –
server.py
client.py
ip_port_gen.py
README.md

Step 2:
Open one instance of the terminal in the same folder in which the abovementioned files are present. Run the command “python server.py”.
If you get the following message –
“Server is listening to incoming connection requests. Currently on standby!”
… your code has successfully run and the instance of the terminal is acting as a server
and is waiting for the clients to join.

Step 3: 
Run another instance of the terminal in the same folder and run the command
“python client.py”.
If you get the following message –
“Vehicle has started connection to the server ...”
…. your code has successfully created an instance of a client. It will now ask if you
want this instance of the client to a SOS responder or not. Now that is up to you. If you
say Y (yes), any SOS message sent by any instance of the client will be visible to these
SOS responders only (to prevent panic in the real-world scenario). If you say N (no), it
will act as a normal vehicle that can send and receive messages to and from the network.

Step: To create another instance of a client, just repeat Step 3 and answer the SOS
responder question based on your need.

Detail: There are specific messages which when sent from a non-SOS Responder client,
will trigger the SOS Alert that will be broadcasted to all the SOS Responders. Check
the code for further clarity.

Test Cases: Try the following keywords (case sensitive) in order to check if the code is
behaving as it should.

1. ACCIDENT - the code should recognise this as a SOS alert and will display a message on the
server screen and the screen of every instance of the client that is a SOS responder only (message 
should not be displayed on the screen of the non SOS responders)(to prevent panic among the others)

2. MALFUNCTION - the code should recognise this as a SOS alert and will display a message on the
server screen and the screen of every instance of the client that is a SOS responder only (message 
should not be displayed on the screen of the non SOS responders)(to prevent panic among the others)

3. TRAFFIC_AHEAD - the code should not recognise this as a SOS alert and will display this same message
on the screen of every instance of the client that is not a SOS responder only (message should not be
displayed on the screen of the server and the SOS responder)(for privacy & security and to prevent
the redundancy of data for others)

4. DIVERSION_AHEAD - the code should not recognise this as a SOS alert and will display this same message
on the screen of every instance of the client that is not a SOS responder only (message should not be
displayed on the screen of the server and the SOS responder)(for privacy & security and to prevent
the redundancy of data for others)