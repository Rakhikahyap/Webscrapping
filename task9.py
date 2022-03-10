import requests
import json
import os
import time
import random

with open("task5.json","r+")as f:
    f1=json.load(f)
def make_folder(movie_detail):
    random_sec=random.randint(1,3)    
    for detail in movie_detail:

        path="/home/admin123/task9/task9"+detail["name"]+".json"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w")as f_path:
                json.dump(detail,f_path,indent=4)

        time.sleep(random_sec)
make_folder(f1)