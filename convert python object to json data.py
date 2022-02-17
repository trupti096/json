import json
dic={"name":"david","class":"I","age":6}
with open("trupti1.json","w") as file:
    json.dump(dic,file,indent=4)
    print(dic)