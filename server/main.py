import socket
server_ip="0.0.0.0"
server_port=1244

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.listen(10)
