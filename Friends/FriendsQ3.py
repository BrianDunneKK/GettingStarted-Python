friends = []
keep_asking = True
while keep_asking:
  name = input("Enter friend's name: ")
  if name == '':
    keep_asking = False
  else:
    friends.append(name)

longest_name = ""
for each_name in friends:
    if len(each_name) > len(longest_name):
        longest_name = each_name
print('Longest name: ' + longest_name)
