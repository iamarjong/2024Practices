
import socket 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.bind(("0.0.0.0",54321))
    data, addr = s.recvfrom(1024)
    print(addr, '說了:',data) 
