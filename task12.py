import requests
import json
from bs4 import BeautifulSoup

def scrape_movie_cast(url):
    url=requests.get(url)
    soup=BeautifulSoup(url.text,'html.parser')
    main_div=soup.find('div',class_='castSection')
    div=main_div.find_all("div",class_="cast-item media inlineBlock")
    div2=main_div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    
    list=[]
    for i in div:
        dict1={}
        cast=i.find("a")["href"][11:]
        dict1["Name"]=cast
        list.append(dict1)
    for i in  div2:
        dict2={}
        cast=i.find("a")["href"][11:]
        dict2["Name"]=cast
        list.append(dict2)
    with open("task12.json","w")as file:
        json.dump(list,file,indent=4)
    return list
scrape_movie_cast( "https://www.rottentomatoes.com/m/toy_story_4")