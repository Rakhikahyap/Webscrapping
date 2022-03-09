from task2 import scrap_top_list
import json
details=scrap_top_list()
def group_by_decade(movies):
    moviedic={}
    list=[]
    list1=[]
    for i in movies:
        # print(i)
        for j in i:
            # print(i[j])
            if j=="Year":
                # print(j)
                if i[j] not in list1:
                    list1.append(i[j])
    list1.sort()
    # print(list1)
    for i in list1:
        modul=i%10
        mo=i-modul
        if mo not in list:
            list.append(mo)
    for x in list:
        moviedic[x]=[]
    # print(moviedic)
    for x in list:
        mod=x+9
        for i in movies:
            for j in i:
                if j=="Year":
                    if i[j]<=mod and i[j]>=x:
                        moviedic[x].append(i)
    
    with open("task3.json","w")as file:
        json.dump(moviedic,file,indent=6)


    return moviedic



group_by_decade(details)
