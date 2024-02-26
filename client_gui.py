"""
FTP Application with DHCP and DNS Client Integration

This script provides a GUI for interacting with three separate client functionalities:
- DHCP client for IP address configuration.
- DNS client for domain name resolution.
- FTP application client for file transfer operations.

The GUI is built using Tkinter, offering a user-friendly interface to perform actions such as
requesting an IP address from a DHCP server, resolving a domain name through a DNS query, and
performing various file transfer operations (upload, download, list, delete) with an FTP server.

Functions:
- submit_dhcp(client, label): Performs a DHCP request to obtain an IP address and updates the GUI.
- click_dhcp(): Initializes the DHCP client GUI window.
- submit(client_dns, entry, label): Sends a DNS query and displays the result in the GUI.
- click_dns(): Initializes the DNS client GUI window.
- click_stop(client_app): Toggles the FTP operation (uploading/downloading) on and off.
- click_downloadFile(client_app): Opens a dialog for file selection and downloads the selected file.
- click_uploadFile(client_app): Opens a dialog for file selection and uploads the selected file.
- click_getList(client_app): Displays a list of files available on the server.
- click_disconnected(client_app, window_app): Disconnects the client from the server and closes the application window.
- click_deleteFile(client_app): Opens a dialog for file selection and deletes the selected file from the server.
- click_app(window): Initializes the FTP application client GUI window.
- logOut(window): Logs out the user and closes the application window.
- start(): Initializes the main GUI window allowing the user to choose between DHCP, DNS, and FTP client functionalities.

The script demonstrates the integration of network clients into a single application,
showcasing how different network protocols and operations can be managed through a unified interface.
"""

from tkinter import *
from client_dhcp import client_dhcp  # Ensure this module exists and is correctly implemented
import client_dns as dns  # Ensure this module exists and is correctly implemented
import client_app as app  # Ensure this module exists and is correctly implemented
import os
from tkinter import filedialog
from tkinter import messagebox


def submit_dhcp(client, label):
    """
    Sends a DHCP discovery request to obtain an IP address and updates the GUI with the response.
    
    This function is called when the user clicks the "Enter" button in the DHCP window. It uses the
    `client_dhcp` instance to send a DHCP discovery message to the DHCP server. The server's response,
    presumably an IP address, is then displayed in the specified label widget in the GUI.
    
    Parameters:
    - client: An instance of the `client_dhcp` class that handles DHCP communication.
    - label: The Tkinter Label widget where the DHCP server's response will be displayed.
    """
    # Send a DHCP discovery message to obtain an IP address.
    ip_domain_name = client.get_ip()
    
    # Update the GUI label with the obtained IP address.
    label.config(text=ip_domain_name)

def click_dhcp():
    """
    Initializes and displays the DHCP client window.
    
    This function is triggered when the user selects the DHCP CLIENT option from the main window.
    It sets up a new window dedicated to DHCP operations, displaying a welcoming message and an "Enter"
    button that the user can click to initiate a DHCP discovery request.
    """
    print("You clicked on the DHCP server button")
    
    # Create an instance of the DHCP client.
    client = client_dhcp()
    
    # Setup the DHCP window.
    window_dhcp = Tk()
    window_dhcp.geometry("900x900")
    window_dhcp.title("DHCP")
    
    # Create and configure a label with a welcoming message.
    label = Label(window_dhcp, text="Welcome to the DHCP server\n ",
                  font=('Ariel', 30, 'bold'), fg='black', bg='#8f9394',
                  width=200, height=850)
    
    # Create an "Enter" button that, when clicked, calls submit_dhcp() to send a DHCP discovery message.
    button = Button(window_dhcp, text="Enter", command=lambda: submit_dhcp(client, label))
    
    # Display the button and label in the window.
    button.pack()
    label.pack()
    


########################################################################################################################
########################################################################################################################



def submit(client_dns, entry, label):
    """
    Submits a DNS query and updates the GUI with the obtained IP address or domain name.
    
    This function fetches the user's input (a domain name) from the entry widget, sends it as a DNS
    query through the `client_dns` instance, and then updates the specified label widget with the
    response, which could be an IP address associated with the domain name.
    
    Parameters:
    - client_dns: An instance of the `client_dns` class that handles DNS queries.
    - entry: The Tkinter Entry widget where the user inputs the domain name.
    - label: The Tkinter Label widget where the DNS query result will be displayed.
    """
    # Fetch the user's input (domain name) from the entry widget.
    text = entry.get()
    
    # Send a DNS query with the entered domain name and receive the IP/domain name response.
    ip_domain_name = client_dns.get_req(text)
    
    # Update the GUI label with the DNS query result.
    label.config(text=ip_domain_name)

def click_dns():
    """
    Initializes and displays the DNS client window.
    
    This function creates a new window for DNS query operations when the user selects the DNS CLIENT
    option from the main application window. It sets up the window with a welcoming message, an entry
    widget for the user to input a domain name, and an "Enter" button to submit the DNS query.
    """
    # Initialize a new instance of the DNS client.
    client_dns = dns.client_dns()
    
    # Setup the DNS window.
    window_dns = Tk()
    window_dns.geometry("900x900")
    window_dns.title("DNS")
    
    # Create and configure a label with a welcoming message for the DNS window.
    label = Label(window_dns, text="Welcome to the DNS server\n ",
                  font=('Ariel', 30, 'bold'), fg='black', bg='#8f9394',
                  width=200, height=850)
    
    # Create an entry widget for user input (domain name).
    entry = Entry(window_dns)
    
    # Create an "Enter" button that, when clicked, calls the submit function to process the DNS query.
    button = Button(window_dns, text="Enter", command=lambda: submit(client_dns, entry, label))
    
    # Display the entry widget, button, and label in the window.
    entry.pack()
    button.pack()
    label.pack()



########################################################################################################################
########################################################################################################################



def click_stop(client_app):
    """
    Toggles the FTP operation (uploading or downloading) on and off.
    
    This function changes the state of the `stop_ftp` flag within the `client_app` instance.
    When called, it inverses the flag's boolean value, effectively stopping or resuming FTP operations.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    """
    # Toggle the stop_ftp flag to stop or resume FTP operations.
    client_app.stop_ftp = not client_app.stop_ftp
    print(f"FTP operations stopped: {client_app.stop_ftp}")

def click_downloadFile(client_app):
    """
    Initiates the file download process from the server.
    
    This function opens a file dialog for the user to select a file from the server's directory.
    Upon file selection, it triggers the download operation and displays a message with the outcome.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    """
    # Create and hide the download window.
    window_downloadFile = Tk()
    window_downloadFile.withdraw()
    
    # Open a file dialog for the user to select a file to download.
    file_path = filedialog.askopenfilename(initialdir="server_files")
    if file_path:
        # Extract the file name from the selected path and initiate the download.
        file_name = os.path.basename(file_path)
        msg = client_app.downloadFile(file_name)
        
        # Show the outcome of the download operation in a message box.
        messagebox.showinfo("Download Status", msg)

def click_uploadFile(client_app):
    """
    Initiates the file upload process to the server.
    
    Opens a file dialog for the user to select a local file to be uploaded to the server.
    After file selection, it triggers the upload operation and displays a message with the outcome.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    """
    # Create and hide the upload window.
    window_uploadFile = Tk()
    window_uploadFile.withdraw()
    
    # Open a file dialog for the user to select a file to upload.
    file_path = filedialog.askopenfilename()
    if file_path:
        # Initiate the upload of the selected file and display the outcome in a message box.
        msg = client_app.uploadFile(file_path)
        messagebox.showinfo("Upload Status", msg)

def click_getList(client_app):
    """
    Displays a list of files available on the FTP server.
    
    This function fetches the list of files from the server and displays it in a new window.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    """
    # Setup the window for displaying the list of server files.
    window_getList = Tk()
    window_getList.geometry("900x900")
    window_getList.title("List of the file server")
    
    # Fetch and display the list of files from the server.
    list_files = client_app.get_list()
    label = Label(window_getList,
                  text=f"List of files on the server:\n\n{list_files}\n",
                  font=('Ariel', 30, 'bold'), fg='black', bg='#8f9394',
                  width=900, height=900)
    label.pack()



def click_disconnected(client_app, window_app):
    """
    Handles the disconnection of the client from the FTP server and closes the application window.
    
    This function calls the `disconnected` method of the `client_app` instance to cleanly
    disconnect from the FTP server. It then destroys the application window, effectively
    closing the application. Lastly, it restarts the application by calling the `start` function.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    - window_app: The main application window instance to be closed upon disconnection.
    """
    # Disconnect the client from the FTP server.
    client_app.disconnected()
    
    # Destroy the application window to close the application.
    window_app.destroy()
    
    # Log the disconnection and restart the application.
    print("The client has been disconnected")
    start()

def click_deleteFile(client_app):
    """
    Initiates the process to delete a file from the FTP server.
    
    Opens a file dialog allowing the user to select a file from the server's directory to be deleted.
    After file selection, it triggers the deletion operation on the server and displays a message box
    with the outcome of the deletion.
    
    Parameters:
    - client_app: An instance of the `client_app` class handling FTP operations.
    """
    # Create and hide the file deletion window.
    window_deleteFile = Tk()
    window_deleteFile.withdraw()
    
    # Open a file dialog for the user to select a file from the server to delete.
    file_path = filedialog.askopenfilename(initialdir="server_files")
    if file_path:
        # Extract the file name from the selected path and initiate the deletion.
        file_name = os.path.basename(file_path)
        msg = client_app.deleteFile(file_name)
        
        # Show the outcome of the deletion operation in a message box.
        messagebox.showinfo("Deletion Status", msg)



########################################################################################################################
########################################################################################################################



def click_app(window):
    """
    Initializes and displays the main window of the FTP application.
    
    This function is called when the user chooses to interact with the FTP application from
    the main menu. It closes the current window (main menu), opens a new window for the FTP
    application, and sets up various FTP operation buttons (e.g., upload, download, delete, list files).
    
    Parameters:
    - window: The current Tkinter window instance, typically the main menu, to be closed.
    """
    # Destroy the current window to return to the main application window.
    window.destroy()
    
    # Initialize a new window for the FTP application.
    window_app = Tk()
    window_app.geometry("900x900")
    window_app.title("FTP Application")
    
    # Create an instance of the FTP client application.
    client_app = app.client_app()

    # Set up a welcoming label at the top of the FTP application window.
    label = Label(window_app,
                  text="Welcome to the Application server\nthis is FTP server\n",
                  font=('Ariel', 30, 'bold'), fg='black', bg='#8f9394',
                  width=150, height=850)
    label.pack()

    # Define buttons for various FTP operations and position them within the window.
    button_getList = Button(window_app, text='Get list of the server files',
                            command=lambda: click_getList(client_app),
                            font=("Comic Sans", 18), fg="green", bg='black',
                            activeforeground="black", relief=RAISED, bd=20)
    button_deleteFile = Button(window_app, text='Delete file from the server files',
                               command=lambda: click_deleteFile(client_app),
                               font=("Comic Sans", 18), fg="green", bg='black',
                               activeforeground="black", relief=RAISED, bd=20)
    button_uploadFile = Button(window_app, text='Upload a file to the server',
                               command=lambda: click_uploadFile(client_app),
                               font=("Comic Sans", 18), fg="green", bg='black',
                               activeforeground="black", relief=RAISED, bd=20)
    button_downloadFile = Button(window_app, text='Download a file from the server',
                                 command=lambda: click_downloadFile(client_app),
                                 font=("Comic Sans", 18), fg="green", bg='black',
                                 activeforeground="black", relief=RAISED, bd=20)
    button_stop = Button(window_app, text='Stop the downloading or uploading',
                         command=lambda: click_stop(client_app),
                         font=("Comic Sans", 18), fg="green", bg='black',
                         activeforeground="black", relief=RAISED, bd=20)
    button_disconnect = Button(window_app, text='Disconnect from the server',
                               command=lambda: click_disconnected(client_app, window_app),
                               font=("Comic Sans", 18), fg="green", bg='black',
                               activeforeground="black", relief=RAISED, bd=20)

    # Position buttons within the window.
    button_getList.place(x=75, y=25)
    button_deleteFile.place(x=75, y=125)
    button_uploadFile.place(x=75, y=225)
    button_downloadFile.place(x=425, y=25)
    button_disconnect.place(x=480, y=125)
    button_stop.place(x=450, y=225)



########################################################################################################################
########################################################################################################################



def logOut(window):
    """
    Logs out the user and closes the application window.
    
    This function prints a log-out message to the console and destroys the Tkinter window,
    effectively closing the application GUI.

    Parameters:
    - window: The current Tkinter window instance to be closed.
    """
    print("The client Log Out")
    window.destroy()



def start():
    """
    Initializes the main application window and displays the server selection options.
    
    This function creates the main window of the application, setting its size, title, and
    initial welcoming message. It then adds buttons that allow the user to choose between
    different server functionalities (DHCP, DNS, FTP application). Each button is configured
    to call a specific function that handles the chosen functionality.

    No parameters.
    """
    # Instantiate the main application window.
    window = Tk()
    window.geometry("900x900")
    window.title("FTP Application")

    # Create a label with a welcoming message and instructions.
    label = Label(window,
                  text="Welcome to the final project\nin communication networks\nplease choose which\nserver you want to connect",
                  font=('Ariel', 40, 'bold'), fg='black', bg='#8f9394',
                  width=150, height=100)
    label.pack()

    # Define and place buttons for choosing between DHCP client, DNS client, and FTP application functionalities.
    button_dhcp_client = Button(window, text='DHCP CLIENT', command=click_dhcp,
                                font=("Comic Sans", 30), fg="green", bg='black',
                                activeforeground="black", relief=RAISED, bd=20)
    button_dns_client = Button(window, text='DNS CLIENT', command=click_dns,
                               font=("Comic Sans", 30), fg="green", bg='black',
                               activeforeground="black", relief=RAISED, bd=20)
    button_application_client = Button(window, text='APPLICATION CLIENT', command=lambda: click_app(window),
                                       font=("Comic Sans", 30), fg="green", bg='black',
                                       activeforeground="black", relief=RAISED, bd=20)
    button_logOut = Button(window, text='Log Out', command=lambda: logOut(window),
                           font=("Comic Sans", 30), fg="green", bg='black',
                           activeforeground="black", relief=RAISED, bd=20)

    # Position buttons within the main window.
    button_dhcp_client.place(x=75, y=25)
    button_dns_client.place(x=475, y=25)
    button_application_client.place(x=75, y=175)
    button_logOut.place(x=600, y=175)

    # Run the main event loop to listen for events and display the window.
    window.mainloop()
    
if __name__ == "__main__":
    start()

