import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #UDP Protocol
ip_address = '127.0.0.1'
port_no = 2525      # 0  -  65353

complete_address = (ip_address,port_no)
s.bind(complete_address)

print('hey i am reciving your message .....')
while True :
    message = s.recvfrom(100)

    sender_address = message[1][0]      #127.0.0.1
    recive_message = message[0]

    decrypted_message = recive_message.decode('ascii')
    print(decrypted_message)

    with open(sender_address +'.txt','a+') as file:     #127.0.0.1.txt
        file.write(decrypted_message +'\n')
