import tkinter
import threading
from network import network

root = tkinter.Tk()
root.geometry("600x520")
root.title("chat app")
server_ip = "169.254.31.1"
port = 3001
username = input("Enter user name: ")

username_display = tkinter.Label(root, text="User: " + username, font=("Calibri 16"))
username_display.grid(row=1)

list1 = tkinter.Listbox(root, width=100, height=24)
list1.grid(row=3)

net1 = network(server_ip, port, list1, username)
net1.connect()

chat2 = tkinter.Entry(root, width=50, font=("Calibri 14"))
chat2.grid(row=2)
chat2.insert(0, "RECEIVER'S Name")

chat = tkinter.Entry(root, width=55, font=("Calibri 14"))
chat.grid(row=4)

def msg_send():
    net1.send(chat2.get(), chat.get())
    chat.delete(0, "end")

btn = tkinter.Button(root, width=50, text="SEND", command=msg_send, font=("Calibri 16"))
btn.grid(row=5)

root.mainloop()