import socket
import threading
server_ip="127.0.0.1"
server_port=1254
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.bind((server_ip, server_port))
    s.listen(5)


except Exception as e:
    print(f"One error ocurred:{e}")

def handVictim(cx):
    """_summary_:handling each victim with multitheard
    
    
    """
    print(cx)
while True:
    conn,detail=s.accept()
    if conn:
        t=threading.Thread(target=handVictim, args=(conn,))
        t.start()





