import socket
from datetime import datetime

server_address = ('localhost', 1234)
max_size = 1000

print("Starting the server at", datetime.now())
print("Wating for a client to call.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
server.bind(server_address) # server_address 정보로 바인딩
server.listen(5) # 클라이언트 접속을 기다림, 전달인자는 최대 연결 수

client, addr = server.accept() # 접속이 연결되면 튜플 형태로 client의 정보를 가져옴
data = client.recv(max_size) # 클라이언트로부터 전송된 데이터를 data 변수에 저장

print("At", datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?') # 클라이언트에게 바이트 메시지 전송
client.close() # 클라이언트 연결 닫음
server.close() # 서버 연결 닫음