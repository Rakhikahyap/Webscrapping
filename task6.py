import json
with open("task5.json","r+") as file:
    movie_data=json.load(file)
    # print(movie_data)
def  analyse_movies_language():
    count={}
    list=[]
    for i in movie_data:
        # print(i)
        if "language" in i:
            l=i["language"]
    # print(list)
            if l in count:
                count[l]=count[l]+1
            if l not in count:
                count[l]=1
    with open("task6.json","w+") as file1:
        json.dump(count,file1,indent=4)
        # return count
analyse_movies_language() 
