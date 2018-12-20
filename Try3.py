import time as t
from datetime import datetime as dt

Path = r"C:\Windows\System32\drivers\etc\hosts"
Target = "127.0.0.1"
WBList = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Not Fun")
        with open(Path,'r+') as FileVar:
            Content = FileVar.read()
            for website in WBList:
                if website in Content:
                    pass
                else:
                    FileVar.write(Target+" "+ website+"\n")
    else:
        with open(Path,'r+') as FileVar:
            Lines = FileVar.readlines()
            FileVar.seek(0)
            for line in Lines:
                if not any(website in line for website in WBList):
                    FileVar.write(line)
            FileVar.truncate()
        print("Fun")
    t.sleep(5)

