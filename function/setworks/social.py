all_user=["mammotty","mohanal","prithvi","asif","dq","fahad","nivin"]
nivin_friends=["asif","dq","fahad"]
dq_friends=["mammotty","mohanal","asif","fahad"]

st_dq_friends=set(dq_friends)
st_all_user=set(all_user)
st_nivin_friends=set(nivin_friends)

# suggestions=st_all_user.difference(st_nivin_friends)
# suggestions.discard("nivin")
# print(suggestions)

mutual=st_nivin_friends.intersection(st_dq_friends)
print(mutual)

