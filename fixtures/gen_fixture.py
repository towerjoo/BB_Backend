from skeleton import items
from follow_relation import relation
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
rel = ""
for i in range(1, 101):
    import random
    r = range(1,101)
    f_id = random.choice(r)
    r.remove(f_id)
    ff_id = random.choice(r)
    data = {
        "id" : str(i),
        "follower" : str(f_id),
        "followee" : str(ff_id),
    }
    item  = relation % data
    rel += item
ret = """[
%s
%s
]"""
print ret % (out, rel[:-2])
    

        
        
        
