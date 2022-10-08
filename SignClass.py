class BusSign:
    def __init__(self, seats, standing = 0):
        self.seats = seats
        self.standing = standing
        self.passengers = 0
        print(f"This bus has {self.seats} seats and room for {self.standing} standing.")
        
    def enter(self):
        if self.passengers < self.seats:
            print("Have a seat!")
        elif self.passengers < (self.seats + self.standing):
            print("You'll have to stand")
        else:
            print("Sorry ... we're full")
        if self.passengers <  (self.seats + self.standing):
            self.passengers += 1

    def leave(self):
        if self.passengers == 0:
            print("There's nobody on the bus!")
        else:
            self.passengers -= 1
            print("Goodbye")


print("\n--- Bus 1 ---")
bus1 = BusSign(5)
for i in range(7):
    bus1.enter()

bus1.leave()
bus1.enter()

for i in range(6):
    bus1.leave()


print("\n--- Bus 2 ---")        
bus2 = BusSign(5, 2)
for i in range(10):
    bus2.enter()

bus2.leave()
bus2.enter()

for i in range(8):
    bus2.leave()
