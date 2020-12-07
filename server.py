import socket
import threading
import pickle

server_ip = socket.gethostbyname(socket.gethostname())
port = 3001
list_of_client_con = []
list_of_client_name = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
print("SERVER STARTED...")

def handle_client(conn, addr):
    connected = True
    while connected:
        msg = pickle.loads(conn.recv(1024))
        if "name_of_user" in msg:
            print(list_of_client_name)
            list_of_client_name.append(msg["name_of_user"])
        else:
            if msg["msg"]:
                if(msg["msg"] == "DISCONNECT"):
                    connected = False
                print(msg["name"] + ": " + msg["msg"])
                print(list_of_client_name)
                if msg["id"]:
                    d = {"name": msg["name"], "msg": msg["msg"]}
                    data = pickle.dumps(d)
                    print(list_of_client_name.index(msg["id"]))
                    index_of_receiver = list_of_client_name.index(msg["id"])
                    list_of_client_con[int(index_of_receiver)].send(data)
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        list_of_client_con.append(conn)
        print(addr[0] + ": connected")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start()