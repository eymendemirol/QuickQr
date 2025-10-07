#Libraries
import qrcode
from tkinter import *
import os
from tkinter import filedialog
import sys
import os

#Main Window Settings
root = Tk()
root.geometry("300x310")
root.title("QR Code Generator")
root.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

try:
    icon_path = resource_path("logo.ico")
    root.iconbitmap(icon_path)
except Exception as e:
    try:
        icon_path = resource_path("logo.png")
        logo_img = PhotoImage(file=icon_path)
        root.iconphoto(True, logo_img)
    except:
        pass

#Object
qr = qrcode.QRCode(version=3, box_size=20, border=10)
selected_path = StringVar()
selected_path.set(os.getcwd())
link_var = StringVar()
filename_var = StringVar()

#Functions
def browse_directory():
    directory = filedialog.askdirectory(initialdir=selected_path.get(), title="Select save directory")
    if directory:
        selected_path.set(directory)
        path_label.config(text="Selected directory:"+os.path.basename(directory))

def apply_dark_theme(widget):
    widget.config(bg="#2f2f2f")
    for child in widget.winfo_children():
        cls = child.winfo_class()
        try:
            if cls == "Label":
                child.config(bg="#2f2f2f", fg="#ffffff")
            elif cls == "Button":
                child.config(bg="#3a3a3a", fg="#ffffff", activebackground="#505050")
            elif cls == "Entry":
                child.config(bg="#4a4a4a", fg="#ffffff", insertbackground="#ffffff")
        except:
            pass
        apply_dark_theme(child)

def show_current():
    current_link = link_entry.get()
    current_name = filename_entry.get()
    currentlink_label.config(text="Current link:\n"+current_link)
    filename_label.config(text="Current file name:\n"+current_name)
    filename_label.after(100)
    currentlink_label.after(100, show_current)

def create():
    link = link_entry.get()
    name = filename_entry.get()
    if not link:
        debug_label.config(text="Enter link !")
        debug_label.after(3000, lambda: debug_label.config(text="Debugger"))
        return
    if not name:
        debug_label.config(text="Enter file name !")
        debug_label.after(3000, lambda: debug_label.config(text="Debugger"))
        return
    file_path = os.path.join(selected_path.get(), name+".png")
    qr.clear()
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    link_entry.delete(0,END)
    filename_entry.delete(0, END)

#Widgets
link_label = Label(root, text="Enter a link for QR code")
link_label.pack(pady=5)
link_entry = Entry(root)
link_entry.pack(pady=5)
create_button = Button(root, text="Create!", command=create)
create_button.pack(pady=5)
currentlink_label = Label(root, text="Current link:")
currentlink_label.pack(pady=5)
filename_label = Label(root, text="Current file name")
filename_label.pack(pady=5)
filename_entry = Entry(root)
filename_entry.pack(pady=5)
browse_button = Button(root, text="📁Select folder", command=browse_directory)
browse_button.pack(pady=5)
path_label = Label(root, text="Selected directory: Current directory ")
path_label.pack(pady=5)
debug_label = Label(root, text="Debugger")
debug_label.pack(pady=5)

#Start application
apply_dark_theme(root)
show_current()
root.mainloop()