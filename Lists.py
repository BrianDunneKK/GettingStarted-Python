my_dojonames = ["Chris", "Alice", "Bob", "Emma", "Danny"]
print(my_dojonames)
names_count = len(my_dojonames)
print("There are "+str(names_count)+" names.")

print("The first name is " + my_dojonames[0])
print("The third name is " + my_dojonames[2])
print("The last name is " + my_dojonames[-1])

my_dojonames.append("Fred")
my_dojonames.remove("Bob")
print(my_dojonames)

my_dojonames.sort()
print(my_dojonames)
my_dojonames.reverse()
print(my_dojonames)