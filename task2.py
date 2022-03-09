from task1 import scrap_top_list
import json


collect_of_task_1=scrap_top_list()
def group_by_year(movies):
    years=[]
    
    for i in movies:
        year=i["Year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i['Year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("taks2.json","w")as f:
        json.dump(movie_dict,f,indent=6)

    return movie_dict

group_by_year(collect_of_task_1)






 
        






