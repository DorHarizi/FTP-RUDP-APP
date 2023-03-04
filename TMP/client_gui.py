from tkinter import *


def click():
    print("you click on bottom")


# instantiate an instance of window
window = Tk()
window.geometry("900x900")
window.title("FTP Application")

button_dhcp_server = Button(window,
                            text='DHCP SERVER',
                            command=click,
                            font=("Comic Sans", 30),
                            fg="green",
                            bg='black',
                            activeforeground="black")


button_dns_server = Button(window,
                           text='DNS SERVER',
                           command=click,
                           font=("Comic Sans", 30),
                           fg="green",
                           bg='black',
                           activeforeground="black")


button_application_server = Button(window,
                                   text='APPLICATION SERVER',
                                   command=click,
                                   font=("Comic Sans", 30),
                                   fg="green",
                                   bg='black',
                                   activeforeground="black")

button_dhcp_server.place(x=240, y=0)
button_dns_server.place(x=250, y=150)
button_application_server.place(x=150, y=300)

# place window on the computer screen, listen for events
window.mainloop()
