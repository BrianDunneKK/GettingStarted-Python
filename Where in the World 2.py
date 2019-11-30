import csv
import webbrowser
from random import randint


countries = []
with open('GettingStarted-Python\\Countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    countries.extend(reader)
for c in countries:
    c["Population"] = int(c["Population"])

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
print("Opening captal in Google maps ...\n")
url = "https://www.google.com/maps/search/?api=1&query={},{}".format(c["CapitalLatitude"], c["CapitalLongitude"])
webbrowser.open(url)