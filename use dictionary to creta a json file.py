import json
dic={
"shopping_list":
{
"choco":"15",
"Biscuits":"50",
"Diary_milk":"30",
"ice_cream":"20",
}
}
with open("trupti9.json","w") as file:
    json.dump(dic,file,indent=4)
    print(dic)