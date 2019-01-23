import socket

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# request connection
host, port = ("baidu.com", 443)
client.connect((host, port))

# send request
client.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

data = client.recv(4096)
print(data)
with open("sina.txt", "wb") as f:
    f.write(data)
print('done')
