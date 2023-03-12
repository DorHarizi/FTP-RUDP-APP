import socket
import server_dns
import client_dns
# # the domain name to lookup
# domain_name = "github.com"
#
# # perform a DNS lookup for the domain name
# ip_address = socket.gethostbyname(domain_name)
#
# # print the IP address
# print(f"The IP address of {domain_name} is {ip_address}")

#israel = server_dns.server_dns()
#israel = client_dns.client_dns()


#
import server_app as app

israel = app.server_app()
print(f"{israel.list_files}")
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import os
#
# # Create a new Tkinter window
# root = tk.Tk()
# root.withdraw()
#
# root2 = tk.Tk()
# messagebox.showinfo("Title", "massege box!!")
# # Set the initial directory to a fixed folder on the server
# initial_dir = "server_files"
# file_path = filedialog.askopenfilename(initialdir=initial_dir)
#
# # Delete the selected file
# if file_path:
#     file_name = os.path.basename(file_path)
#
#     print(f"{file_name} has been deleted.")
# else:
#     print("No file was selected.")
#
#     root2.mainloop()