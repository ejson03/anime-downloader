import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import sys, shutil, os, requests, threading
from pySmartDL import SmartDL
from bs4 import BeautifulSoup
import concurrent.futures
import urllib.request
# import progressbar

# def Download_Progress(block_num, block_size, total_size):
#     downloaded = block_num * block_size
#     progress = int((downloaded/total_size)*100)
#     print ("Download Progress",str(progress),"%")

# pbar = None

# def show_progress(block_num, block_size, total_size):
#     global pbar
#     if pbar is None:
#         pbar = progressbar.ProgressBar(maxval=total_size)
#     pbar.start()
#     downloaded = block_num * block_size
#     if downloaded < total_size:
#         pbar.update(downloaded)
#     else:
#         pbar.finish()
#         pbar = None

def download(downloads):
    try:
        urllib.request.urlretrieve(downloads[0], downloads[1]) 
        print(f"{downloads[2]} done")
        return
    except Exception as e:
        # print(f"{downloads[2]} not downloaded")
        # print(e)
        return

def parellel_downloader(downloads):
    with concurrent.futures.ThreadPoolExecutor() as exector : 
        futures = []
        for url in downloads:
            futures.append(exector.submit(download, downloads=url))
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url[2], exc))
            else:
                print('%r page is %d bytes' % (url[2], len(data)))
    sys.exit()

def search(anime, root, start, end):
    quality = {
        "480p": [],
        "720p" : []
    }
    downloads = []
    search_name = anime.replace(" ", "-")
    search_url = f"https://gogoanime.sh/{search_name}-dub-episode-"
    req = requests.get(search_url)
    destination = f"{root}/{anime}"
    if not os.path.exists(destination):
        os.mkdir(destination)

    with open(f"{anime}.txt", "a+") as f:

        for episode in range(int(start),int(end)+1):
            episode_url = search_url + str(episode)
            r = requests.get(episode_url)
            soup=BeautifulSoup(r.text,'html.parser')
            links=soup.find_all(target='_blank')
            for link in links:
                l=link.get('href')
                if 'download' in l:
                    r1=requests.get(l)
                    s1=BeautifulSoup(r1.text,'html.parser')
                    l1=s1.find_all('a')
                    for l2 in l1:
                        l3=l2.get('href')
                        des = f"{destination}/{anime}-ep-{episode}.mp4"
                
                        if "480p" in l3:
                            quality["480p"].append([l3,des,f"{anime}-ep-{episode}"])
                            # download([l3,des,f"{anime}-ep-{episode}"])
                        else:
                            if "720p" in l3:
                                quality["720p"].append([l3,des,f"{anime}-ep-{episode}"])
                                # download([l3,des,f"{anime}-ep-{episode}"])
        downloads = quality["480p"] if len(quality["480p"]) > 0 else quality["720p"]   
        for download in downloads:
            f.write(download[0] + "\n")          
        parellel_downloader(downloads)
                            
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

