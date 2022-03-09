import json
from task1 import scrap_top_list
from task4 import scrap_movie_details
with open("task_1_movie_detaits.json","r")as file:
    movie_data=json.load(file)
    # print(movie_data)
def get_movie_list_details ():
    movie=[]
    for i in movie_data:
        url=i["Url"]
        # print(url)
        x=scrap_movie_details(url)
        movie.append(x)
        # print(movie)
    with  open("task5.json","w")as file1:
        json.dump(movie,file1,indent=4)
        return movie

get_movie_list_details ()

    
