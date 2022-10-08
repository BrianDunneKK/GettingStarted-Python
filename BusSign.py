class BusSign:
    def __init__(self, seats, standing = 0):
        self.seats = seats
        self.standing = standing
        self.passengers = 0
        print(f"This bus has {self.seats} seats and room for {self.standing} standing.")

    def any_room(self, num_passengers = 1):
        if num_passengers <= 0:
            # Invalid number of passengers
            return -1
        elif (self.passengers + num_passengers) > (self.seats + self.standing):
            # Not enough room for everyone
            return 0
        elif (self.passengers + num_passengers) <= self.seats:
            # Enough seats for everyone
            return 1
        elif self.passengers < self.seats:
            # Some will get seats and some will have to stand
            return 2
        else:
            # All will have to stand
            return 3
        
    def enter(self, num_passengers = 1):
        status = self.any_room(num_passengers)
        match status:
            case 0:
                msg = "Sorry ... we're full."
            case 1:
                msg = "Have a seat!"
            case 2:
                msg = "Some of you will have to stand."
            case 3:
                msg = "You will have to stand."
            case _:
                msg = "You entered an invalid number of passengers."

        if status > 0:
            self.passengers += num_passengers

        self.display_msg(num_passengers, msg)


    def leave(self, num_passengers = 1):
        if self.passengers == 0:
            msg = "There's nobody on the bus!"
        else:
            self.passengers -= num_passengers
            msg = "Goodbye!"

        self.display_msg(-num_passengers, msg)

    def all_leave(self):
        self.passengers = 0
        self.display_msg(0, "Goodbye everyone")

    def display_msg(self, count, msg):
        if count < 0:
            direction = f"{-count} leaving"
        else:
            direction = f"{count} entering"

        seats_free = self.seats - self.passengers
        if seats_free >= 0:
            standing_room = self.standing
        else:
            seats_free = 0
            standing_room = self.seats + self.standing - self.passengers

        status = f"Passengers = {self.passengers}, Seats free = {seats_free}, Standing room = {standing_room}"

        print(f"{direction}.\t{msg:32} {status}")
