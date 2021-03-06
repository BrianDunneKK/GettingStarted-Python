from random import randint

countries = [
    {"Country":"Ireland", "Continent":"Europe", "Population":4857000,  "Capital":"Dublin"},
    {"Country":"Brazil", "Continent":"South America", "Population":210147125,  "Capital":"Brasilia"},
    {"Country":"Vietnam", "Continent":"Asia", "Population":94569072,  "Capital":"Hanoi"},
    {"Country":"Andorra", "Continent":"Europe", "Population":77281,  "Capital":"Andorra"}
    ]

msg = "The countries in Europe are: "
for c in countries:
    if c["Continent"] == "Europe":
        msg += c["Country"] + ", " 
print(msg+"\n")

largest_country = ""
largest_population = 0
for c in countries:
    if c["Population"] > largest_population:
        largest_country = c["Country"]
        largest_population = c["Population"]
print ("The country with the largest population is " + largest_country + ".\n")

secret_number = randint(0,len(countries)-1)
c = countries[secret_number]
answer = input("What is the capital of " + c["Country"] + "? ")
if answer == c["Capital"]:
    print ("Correct!\n")
else:
    print ("Incorrect ... the capital is " + c["Capital"] + "\n")

