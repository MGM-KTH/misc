# -*- coding: utf-8 -*-

# @author: Martin Runelöv
# Server for the Sokoban homework
# AI

# Protocol:
# 1. Read board ID
# 2. Send board
# 3. Receive solution
# 4. Send response to solution
# OBS: Every line sent to the client has to end with a newline
# (Because "ReadLine" is used in the C++ client)
import socket


def send_board(filename, client):
    """
    Opens a file containing a Sokoban level (board)
    and sends it to the connected client
    """
    try:
        f = open('boards/' + board, 'r')
        for line in f:
            print(line)
            client.send(line)
        f.close()
    except IOError:
        client.send("\n")

host = "localhost"
port = 5555
board = "sokoban1"
s = socket.socket()
s.bind((host, port))

s.listen(5)
while True:
    try:
        client, address = s.accept()
        print("Got Connection from" + str(address))
        # Read board number
        board_no = client.recv(4096)
        send_board(board, client)
        # Read answer
        solution = client.recv(4096)
        print("Answer received from client: \n '" + str(solution) + "'")
        client.send("Received the answer!\n")
        # Close the connection
        print("Closing connection to " + str(address))
        client.close()
    # Catch KeyboardInterrupts like ctrl+C
    except KeyboardInterrupt:
        # Close the socket
        s.close()
