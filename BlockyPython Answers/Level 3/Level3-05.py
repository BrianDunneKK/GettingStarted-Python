friends = []
keep_asking = True
while keep_asking:
  name = input("Enter friend's name: ")
  if name == '':
    keep_asking = False
  else:
    friends.append(name)

sorted_friends = sorted(friends)

for i in range(len(sorted_friends)):
    str = "{}: {}".format(i+1, sorted_friends[i])
    print(str)
