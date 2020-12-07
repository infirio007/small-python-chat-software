import socket
import threading, pickle, tkinter

print("CONNECTED TO THE SERVER.")

class network:
    def __init__(self, server_ip, server_port, list1, name):
        self.server_ip = server_ip
        self.port = server_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.arr_recv = []
        # self.arr_send = []
        self.list1 = list1
        self.name = name

    def connect(self):
        self.client.connect((self.server_ip, self.port))
        self.send_userName()
        thread = threading.Thread(target=self.recev, args=[self.list1])
        thread.start()

    def send_userName(self):
        final_data = pickle.dumps({"name_of_user": self.name})
        self.client.send(final_data)

    def send(self, id, msg):
        if msg:
            encoded_mgs = {"name": self.name, "msg": msg, "id":id}
            final_msg = pickle.dumps(encoded_mgs)
            self.client.send(final_msg)
            self.list1.insert("end", f"{self.name}: {msg}")

    def recev(self, list1):
        while True:
            msg = pickle.loads(self.client.recv(1024))
            if msg["msg"]:
                self.list1.insert("end", str(msg["name"]) + ": " + str(msg["msg"]))