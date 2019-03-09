countries = [
    {"name":"Ireland", "continent":"Europe", "pop":4857000,  "capital":"Dublin"},
    {"name":"Brazil", "continent":"South America", "pop":210147125,  "capital":"Brasilia"},
    {"name":"Vietnam", "continent":"Asia", "pop":94569072,  "capital":"Hanoi"},
    {"name":"Andorra", "continent":"Europe", "pop":77281,  "capital":"Andorra"}
    ]

for c in countries:
    if c["continent"] == "Europe":
        print(c["name"] + " is in Europe")

from random import randint
secret_number = randint(0,3)

c = countries[secret_number]
answer = input("What is the capital of " + c["name"] + "? ")
if answer == c["capital"]:
    print ("Correct!")
else:
    print ("Incorrect ... the capital is " + c["capital"])

largest_country = ""
largest_population = 0
for c in countries:
    if c["pop"] > largest_population:
        largest_country = c["name"]
        largest_population = c["pop"]
print ("The country with the largest population is " + largest_country)
