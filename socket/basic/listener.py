
import socket
HOST, PORT = '192.168.0.198' , 54321 
# HOST, PORT = '192.168.178.44' , 54321 

server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Book".encode(), server_addr)
print('a', end = '') 
