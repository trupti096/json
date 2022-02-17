# take two userinputs
# username and password
# take dict
# if i enterd username and password it should covert the json format


import json
userinputs=input("enter userinput=")
password=input("enter passwod=")
a=[userinputs]
b=[password]
i=0
dict1={ }
dict2={ }
dict3={ }
dict4={ }
dict5={ }
while i<len(a):
    dict1=userinputs
    dict2=password
    i=i+1
dict3["userinputs"]=dict1
dict4["password"]=dict2
dict5.update(dict3)
dict5.update(dict4)

x=json.dumps(dict5)
print(x)
with open("linu2.json","w") as file:
    json.dump(dict5,file,indent=4)
    