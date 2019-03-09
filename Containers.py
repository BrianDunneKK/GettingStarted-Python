for num in range(11):
    print(str(num))
    
print("I can count to ten!")

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
for day in weekdays:
    if day[0] != "S":
        print ( day + " - school day")
    else:
        print ( day + " - weekend")

print (weekdays[3])
#print (weekdays[99])


my_pet = {
    "name" : "Spot",
    "type" : "dog",
    "age"  : 3,
    "eats" : "bones"
}
print(my_pet)

print(my_pet["name"])
print("My pet is " + str(my_pet["age"]) + " years old")

my_pets = [
    {
        "name" : "Spot",
        "type" : "dog",
        "age"  : 3,
        "eats" : "bones"
        },
    {
        "name" : "Fluffy",
        "type" : "rabbit",
        "age"  : 2,
        "eats" : "carrots"
        },
    {
        "name" : "Snap",
        "type" : "crocodile",
        "age"  : 6,
        "eats" : "people"
        }
]

my_pets.pop(2)
my_pets.append({"name":"Goldie", "type":"fish", "age":1, "eats":"fish food"})

for pet in my_pets:
    print("I have a " + pet["type"] + " named " + pet["name"] +
          ". My pet is " + str(pet["age"]) + " years old " +
          "and eats " + pet["eats"] + ".")

