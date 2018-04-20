users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

print(inactive_users)

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

print(inactive_users2)

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

print(usernames)

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

print(usernames2)

#remove negative numbers in a list
def remove_negatives(my_list):
    return list(filter(lambda x: x >= 0, my_list))

print(remove_negatives([-1, 0, 4, 9, -99]))