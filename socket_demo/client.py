import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))


# 接收小于 1024 字节的数据  
data = s.recv(1024)

print('Received', data.decode('utf-8'))

time.sleep(10)

# 发送消息  
message = 'Hello, server!'
s.send(message.encode('utf-8')) 

s.close()