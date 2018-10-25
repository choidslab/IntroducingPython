import socket
from datetime import datetime

server_address = ('localhost', 1234)
max_size = 1000

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
client.connect(server_address) # 서버에 연결
client.sendall(b'Hey!') # 서버에 데이터 전송
data = client.recv(max_size) # 서버로부터 데이터 수신
print('At', datetime.now(), 'someone replied', data)
client.close()

