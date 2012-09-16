from skeleton import items
out = ""
for i in range(1, 101):
    import random
    data = {
        "id" : str(i),
        "username" : "zhutao" + str(i),
        "email": "zhutao%d@gmail.com" % i,
        "group_members" : random.sample(range(1,101), random.randint(3,10)),
        "note_status" : random.choice([1, 2]),
        "shout_type" : random.choice([1, 2]),
        "account_type" : random.choice([1, 2]),
        "gender" : random.choice([1, 2]),
    }
    item = items % data
    out += item
ret = """[
%s
]"""
print ret % out[:-2]
    

        
        
        
