import time
from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=['www.yahoo.com', 'www.facebook.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        with open(host_path,'r+') as file:
            content=file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
