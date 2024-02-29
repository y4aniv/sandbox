vote = {"Bob": 21, "Bill": 10, "Emma": 18, "Donald": 0, "Jack": 5}

for key in vote:
    print(vote[key])

print('')
for key in vote:
    print(key)
print('')
for key in vote:
    print(tuple((key, vote[key])))
print('')
listeTuple = list((key, value) for key, value in vote.items())
print(listeTuple)