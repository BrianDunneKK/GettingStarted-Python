def greet(name):
    print("Hello "+name)
    print("Welcome to the world of Python.")

greet("Donald Duck")

def ask_for_name():
    your_name = input("What is your name? ")
    return your_name

#name = ask_for_name()
#greet(name)

def ask_two_names(pet):
    your_name = input("What is your name? ")
    pet_name = input("What is the name of your pet "+pet+"? ")
    two_names = {
        "person": your_name,
        "pet": pet_name
        }
    return two_names

my_pet = "turtle"
names = ask_two_names(my_pet)
print("Hi " + names["person"] + ", I hear you have a " + my_pet + " named " + names["pet"])
