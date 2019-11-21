friends = []
keep_asking = True
while keep_asking:
  name = input("Enter friend's name: ")
  if name == '':
    keep_asking = False
  else:
    friends.append(name)

sorted_friends = sorted(friends)
str_sorted = ", ".join(sorted_friends[:3])
print('Your top 3 sorted friends are: ' + str_sorted)
