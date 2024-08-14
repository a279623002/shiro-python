import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))

# 设置最大连接数，超过后排队
server_socket.listen(10)

print('服务器启动，等待连接...')

while True:
    client_socket, client_address = server_socket.accept()
    print('连接地址：', client_address)
    msg = '访问服务端成功！' + '\r\n'
    client_socket.send(msg.encode('utf-8'))

    # 接收客户端发送的消息  
    message = client_socket.recv(1024)  # 1024是接收消息的最大字节数  
    print('Received message:', message.decode('utf-8')) 

    client_socket.close()
    break
server_socket.close()