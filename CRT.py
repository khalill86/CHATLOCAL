import socket
import threading
import tkinter as tk
root = tk.Tk()
HOST = "127.0.0.1"
PORT = 1234
def LISTEN_FOR_MESSAGES(client):
    while 1 :
        message= client.recv(2048).decode("utf-8")
        if message != "":
            username = message.split(":")[0]
            content = message.split(":")[1]
            print(f"{username} says: {content}")
        else:
            print("message received from client is empty")

def SEND_MESSAGES(client):

    while 1 :
        messege = input("message:")
        if message != "":
            client.send(messege.encode("utf-8"))
        else:
            print("you can't send empty message")
            exit(0)
def communction_to_server(client):            