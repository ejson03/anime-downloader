import requests
from pySmartDL import SmartDL
import sys
import os
from clint.textui import progress
from bs4 import BeautifulSoup
import shutil

def download(url, dest):
    obj=SmartDL(url, dest)
    obj.start()
    return


def search(anime, d, start, end):
    #anime = input("Enter anime name> " )
    downloads = []
    search_name = anime.replace(" ", "-")
    url= f"https://gogoanime.sh/{search_name}-dub-episode-"
    rq=requests.get(url)
    destination = f"{d}/{anime}"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    for i in range(int(start),int(end)+1):
        u=url+str(i)
        print(u)
        r=requests.get(u)
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
                    if "480p" in l3:
                        print("l3",l3)
                        des = f"{destination}/{anime}-ep-{i}.mp4"
                        download(l3,destination)


