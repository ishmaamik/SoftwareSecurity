import sys #allows system 
import socket #for socket module to execute commands like recv, send, socket connection
import getopt #for parsing the command line- -l, -a, -t stands for what
import threading #for spawning new threads so the processor doesn't get blocked by one process
import subprocess #for getting, sending and storing output

def client_sender(buffer):
    
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET for IPV4 protocol and SOCK_STREAM for TCP
    #Socket module of the socket library takes two args- Internet Address and protocol
    
    try:
        client.connect((target, port))  #connects to a target ip address and port
        while True:
            recv_len= 1
            response=""
        
            while recv_len:
                data= client.recv(4096) #commonly 4096 is the buffer size so client receives 4096 bytes from the server
                recv_len= len(data) #checks for the received length in bytes
                response+= data.decode()   #to the response we add the data after decoding it
                
                if(recv_len<4096):  #if received length is less than 4096, obviously we received the whole data at once 
                    break   #else data is received into chunks of length 4096 byte each
                
                print(response, end="") #end="" to ensure the server response is readable, not broken into lines

                buffer= input("")   #takes input from user as a string
                buffer+= '\n'   #ensures the user input is terminated before sending to server   
                
                #why input at the end? because first website sends us some static output (server) and then client waits for user input
    except:  
        print("[*] Exception! Exiting.")
        client.close()
        

def server_loop():
    global target
    
    if not len(target):
        target= "0.0.0.0" #set for all available network ip address
    
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(target, port)
    server.listen(5)    #listens to 5 connections simultaneously
    while True: #infinite loop, needs to continuously listen for incoming connections
        client_socket, addr= server.accept()
    
        client_thread= threading.Thread(target=client_handler, args=client_socket)
    #target function is the client_handler which handles the client
    #and client_socket is passed to it cause this is how the client and server communicates
        client_thread.start()
    

    