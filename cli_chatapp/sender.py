import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #UDP Protocol

target_ip = '127.0.0.1'
port_no = 2525
target_address = (target_ip,port_no)
 
while True :
    message = input('plz write your message here :')
    encrpt_message = message.encode('ascii')
    s.sendto(encrpt_message,target_address)
