import json
dic={'4':5,'6':7,'1':3,'2':4}
sorted_items=sorted(dic.items())
d=dict(sorted_items)
x=json.dumps(d)
print(x)