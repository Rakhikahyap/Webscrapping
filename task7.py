import json
with open("task5.json","r")as f:
    movie_director=json.load(f)
def analyse_movies_directors():
    count={}
    for i in movie_director:
        if "Director" in i:
            d=i["Director"]
    
            for j in d:
                if j in count:
                    count[j]=count[j]+1
                if j not in count:
                    count[j]=1

    with open("task7.json","w")as f1:
        json.dump(count,f1,indent=4)
analyse_movies_directors()

    
