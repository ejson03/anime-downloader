import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from gogo_spider import search
import sys

def Widgets():
    link_label = Label(root, text="Anime name  :", bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    first_label = Label(root, text="First  :", bg="#E8D579")
    first_label.grid(row=2,
                     column=0,
                     pady=5,
                     padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=first_Episode)
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    last_label = Label(root, text="Last  :", bg="#E8D579")
    last_label.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=last_Epsisode)
    root.linkText.grid(row=3,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=4,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=4,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=2,
                    column=2,
                    pady=3,
                    padx=3)


def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)


def Download():
    name = video_Link.get()
    destination = download_Path.get()
    first = first_Episode.get()
    last = last_Epsisode.get()
    search(name, destination, first, last)


root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Anime downloader")
root.config(background="#000000")
video_Link = StringVar()
download_Path = StringVar()
first_Episode = StringVar()
last_Epsisode = StringVar()
Widgets()
root.mainloop()
