from task4 import scrap_movie_details
from task12 import scrape_movie_cast
import json
def scrap_movie_one(url):
    list=[]
    t4= scrap_movie_details(url)
    t12=scrape_movie_cast(url)
    list.append(t4)
    list.append({"cast":t12})
    with open("tast13.json","w+")as file:
        json.dump(list,file,indent=6)

scrap_movie_one("https://www.rottentomatoes.com/m/toy_story_4")