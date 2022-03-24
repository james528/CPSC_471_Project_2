# udppingserver_no_loss.py
from socket import *
import random
import time


# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:

    rand = random.uniform(10, 40)

    time.sleep(rand)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # The server responds
    serverSocket.sendto(message, address)