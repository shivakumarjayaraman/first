from collections import defaultdict
from operator import itemgetter
from collections import Counter
import re

## Parse out stuff from a file and load data
def loadUsersAndFriendships(fname) :
    pat = re.compile(r"(.*)\s*:(.*)$")
    users = []
    friendships = []
    u2i = defaultdict(list)
    i2u = defaultdict(list)

    id = 0
    with open(fname) as fp :
        for u in iter(fp.readline, "\n") :
            if u.startswith("#") : continue

            mat = pat.match(u)
            interests = list(map(lambda x : x.strip(), mat.group(2).split(",")))
            users.append({'id' : id, 'name' : mat.group(1), 'friends' : []})

            u2i[id].extend(interests)
            for i in interests :
                i2u[i].append(id)
            id += 1

        for f  in iter(fp.readline, "") :
            if f.startswith("#") : continue
            u1, u2 =  f.split(",")
            friendships.append((int(u1), int(u2)))
            users[int(u1)]['friends'].append(users[int(u2)])
            users[int(u2)]['friends'].append(users[int(u1)])


    return users, friendships, u2i, i2u

## Find number of friends for a given user
def numberOfFriends(u) :
    return len(u['friends'])

## Find average # friends for all users
def averageFriends(users) :
    return sum(numberOfFriends(u) for u in users) / len(users)

## Sort people by the number of friends they have
def popularityList(users) :
    return sorted(((u['id'], numberOfFriends(u)) for u in users), key=itemgetter(1), reverse=True)


## Find friend of friends and how strong they are (if a fof is known via multiple 
## friends, count them multiple times)
def fof(users, uid) :
    foaf = (fo['id'] for f in users[uid]['friends'] for fo in f['friends'])
    foaf = filter(lambda x : x != uid and users[x] not in users[uid]['friends'],  foaf)
    
    return Counter(foaf)

##
def whoHasMostCommonInterestsWith(u2i, i2u, uid) :
    return Counter(u for i in u2i[uid] for u in i2u[i] if u != uid)


## Load stuff, so you can play with it
users, f, u2i, i2u = loadUsersAndFriendships("users.txt")
