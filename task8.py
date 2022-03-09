import requests
import os
from task1 import scrap_top_list
data=scrap_top_list()
def get_scrap_movie_details():
    for i in data:
        path="/home/admin123/task8/task8"+i["Movie_Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w+")
            url=requests.get(i["Url"])
            a=create.write(url.text)
get_scrap_movie_details()