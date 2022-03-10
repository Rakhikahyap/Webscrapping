import requests
import json

with open("task5.json","r")as file:
    movie_data=json.load(file)
    print(movie_data)
def  get_movie_list_details():
    c={}
    for i in movie_data:
        # print(i)
        if "language" in i:
            l=i["Genre"]
            for j in l:
                # print(j)
                if j in c:
                    c[j]=c[j]+1
                if j not in c:
                    c[j]=1
    with open("task11.json","w")as file1:
        json.dump(c,file1,indent=6)   
get_movie_list_details()



