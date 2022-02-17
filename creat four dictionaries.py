import json
l1=["neelam","programer","4","2400"]
l2=["komal","trainer","24","20000"]
l3=["anuradha","HR","25","40000"]
l4=["Abhishek","manager","29","63000"]
b=["emp1","emp2","emp3","emp4"]
c=["name","designation","age","salary"]
i=0
dict={ }
dict2={}
dict3={}
dict4={}
dict5={}
for i in range(len(l1)):
    dict[c[i]]=l1[i]
    dict2[c[i]]=l2[i]
    dict3[c[i]]=l3[i]
    dict4[c[i]]=l4[i]

dict5["emp1"]=dict
dict5["emp2"]=dict2
dict5["emp3"]=dict3
dict5["emp4"]=dict4

f=json.dumps(dict5)
print(f)
with open("linu.json","w") as file:
    json.dump(dict5,file,indent=4)
    