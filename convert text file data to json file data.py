import json
d={"name":"gugu","destination":"coder","age":21}
with open("text.json","w")as f:
    json.dump(d,f,indent=4)
    a=json.dumps(d)
    print(a)
    print(type(a))
