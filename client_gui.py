from tkinter import *

import client_app


def click_getList():
    pass


def click_dhcp():
    print("you click on server dhcp button")


def click_dns():
    print("you click on server dns button")


def click_app():
    print("you click on server app button")
    window_app = Tk()
    window_app.geometry("900x900")
    window_app.title("FTP Application")

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
                            command=click_getList,
                            font=("Comic Sans", 18),
                            fg="green",
                            bg='black',
                            activeforeground="black",
                            relief=RAISED,
                            bd=20)

    button_deleteFile = Button(window_app,
                               text='Delete file from the *server files',
                               command=click_dhcp,
                               font=("Comic Sans", 18),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    button_uploadFile = Button(window_app,
                               text='Upload a file to the server',
                               command=click_dhcp,
                               font=("Comic Sans", 18),
                               fg="green",
                               bg='black',
                               activeforeground="black",
                               relief=RAISED,
                               bd=20)

    button_downloadFile = Button(window_app,
                                 text='Download a file from the server',
                                 command=click_dhcp,
                                 font=("Comic Sans", 18),
                                 fg="green",
                                 bg='black',
                                 activeforeground="black",
                                 relief=RAISED,
                                 bd=20)

    button_disconnect = Button(window_app,
                               text='Disconnect from the server',
                               command=click_dhcp,
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
    button_disconnect.place(x=425, y=125)



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
                                command=click_dhcp,
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
