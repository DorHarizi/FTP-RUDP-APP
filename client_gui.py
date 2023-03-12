from tkinter import *

import client_dhcp as dhcp
import client_dns as dns
import client_app as app
import os
from tkinter import filedialog
from tkinter import messagebox


def click_dhcp():
    print("you click on server dhcp button")


########################################################################################################################
########################################################################################################################

def submit(client_dns, entry, label):
    text = entry.get()
    ip_domain_name = client_dns.get_req(text)
    label.config(text=ip_domain_name)


def click_dns():
    print("you click on server dns button")
    client_dns = dns.client_dns()
    window_dns = Tk()
    window_dns.geometry("900x900")
    window_dns.title("DNS")
    label = Label(window_dns,
                  text="Welcome to the DNS server\n ",
                  font=('Ariel', 30, 'bold'),
                  fg='black',
                  bg='#8f9394',
                  width=200,
                  height=850)

    entry = Entry(window_dns)
    button = Button(window_dns, text="Enter", command=lambda: submit(client_dns, entry, label))

    entry.pack()
    button.pack()
    label.pack()


########################################################################################################################
########################################################################################################################
def click_stop(client_app):
    client_app.stop = not client_app.stop
    print(f"{client_app.stop}")


def click_downloadFile(client_app):
    window_downloadFile = Tk()
    window_downloadFile.withdraw()
    initial_dir = "server_files"
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    if file_path:
        file_name = os.path.basename(file_path)
        print(f"{file_name} has been chosen")
        msg = client_app.downloadFile(file_name)
        messagebox.showinfo("title", msg)
        window_downloadFile.mainloop()


def click_uploadFile(client_app):
    print("you selected upload")
    window_uploadFile = Tk()
    window_uploadFile.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"{file_path} has been chosen")
        msg = client_app.uploadFile(file_path)
        messagebox.showinfo("title", msg)
        window_uploadFile.mainloop()


def click_getList(client_app):
    window_getList = Tk()
    window_getList.geometry("900x900")
    window_getList.title("List of the file server")
    list_files = client_app.get_list()
    label = Label(window_getList,
                  text=f"List files of the server:\n\n "
                       f"{list_files}\n",
                  font=('Ariel', 30, 'bold'),
                  fg='black',
                  bg='#8f9394',
                  width=900,
                  height=900)

    label.pack()


def click_disconnected(client_app, window_app):
    client_app.disconnected()
    window_app.destroy()
    print("the client has been disconnected")


def click_deleteFile(client_app):
    window_deleteFile = Tk()
    window_deleteFile.withdraw()
    initial_dir = "server_files"
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    if file_path:
        file_name = os.path.basename(file_path)
        print(f"{file_name} has been chosen")
        msg = client_app.deleteFile(file_name)
        messagebox.showinfo("title", msg)
        window_deleteFile.mainloop()


########################################################################################################################
########################################################################################################################

def click_app():
    print("you click on server app button")
    window_app = Tk()
    window_app.geometry("900x900")
    window_app.title("FTP Application")
    client_app = app.client_app()

    label = Label(window_app,
                  text="Welcome to the Application server\n "
                       "this is FTP server\n",
                  font=('Ariel', 30, 'bold'),
                  fg='black',
                  bg='#8f9394',
                  width=150,
                  height=850)

    button_getList = Button(window_app,
                            text='Get list of the server files',
                            command=lambda: click_getList(client_app),
                            font=("Comic Sans", 18),
                            fg="green",
                            bg='black',
                            activeforeground="black",
                            relief=RAISED,
                            bd=20)

    button_deleteFile = Button(window_app,
                               text='Delete file from the server files',
                               command=lambda: click_deleteFile(client_app),
                               font=("Comic Sans", 18),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    button_uploadFile = Button(window_app,
                               text='Upload a file to the server',
                               command=lambda: click_uploadFile(client_app),
                               font=("Comic Sans", 18),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    button_downloadFile = Button(window_app,
                                 text='Download a file from the server',
                                 command=lambda: click_downloadFile(client_app),
                                 font=("Comic Sans", 18),
                                 fg="green",
                                 bg='black',
                                 activeforeground="black",
                                 relief=RAISED,
                                 bd=20)

    button_stop = Button(window_app,
                         text='Stop the downloading or uploading\n'
                              '',
                         command=lambda: click_stop(client_app),
                         font=("Comic Sans", 18),
                         fg="green",
                         bg='black',
                         activeforeground="black",
                         relief=RAISED,
                         bd=20)

    button_disconnect = Button(window_app,
                               text='Disconnect from the server',
                               command=lambda: click_disconnected(client_app, window_app),
                               font=("Comic Sans", 18),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    label.pack()
    button_getList.place(x=75, y=25)
    button_deleteFile.place(x=75, y=125)
    button_uploadFile.place(x=75, y=225)
    button_downloadFile.place(x=425, y=25)
    button_disconnect.place(x=480, y=125)
    button_stop.place(x=450, y=225)


########################################################################################################################
########################################################################################################################

def start():
    # instantiate an instance of window
    window = Tk()
    window.geometry("900x900")
    window.title("FTP Application")

    label = Label(window,
                  text="Welcome to the final project\n "
                       "in communication networks\n"
                       " please choose which\n"
                       " server you want connect",
                  font=('Ariel', 40, 'bold'),
                  fg='black',
                  bg='#8f9394',
                  width=150,
                  height=100)

    button_dhcp_server = Button(window,
                                text='DHCP SERVER',
                                # command=click_dhcp,
                                font=("Comic Sans", 30),
                                fg="green",
                                bg='black',
                                activeforeground="black",
                                relief=RAISED,
                                bd=20)

    button_dns_server = Button(window,
                               text='DNS SERVER',
                               command=click_dns,
                               font=("Comic Sans", 30),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    button_application_server = Button(window,
                                       text='APPLICATION SERVER',
                                       command=click_app,
                                       font=("Comic Sans", 30),
                                       fg="green",
                                       bg='black',
                                       activeforeground="black",
                                       relief=RAISED,
                                       bd=20)
    label.pack()
    button_dhcp_server.place(x=75, y=25)
    button_dns_server.place(x=475, y=25)
    button_application_server.place(x=175, y=175)

    # place window on the computer screen, listen for events
    window.mainloop()


start()
