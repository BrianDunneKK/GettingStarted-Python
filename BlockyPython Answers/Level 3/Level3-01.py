friends = []
for count in range(3):
  name = input("Enter friend's name: ")
  friends.append(name)
str_friends = ", ".join(friends)
print('Your friends are: ' + str_friends)
