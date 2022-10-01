friends = []
keep_asking = True
while keep_asking:
  name = input("Enter friend's name: ")
  if name == '':
    keep_asking = False
  else:
    friends.append(name)
str_friends = ", ".join(friends)
print('Your friends are: ' + str_friends)
