from BusSign import *


print("\n--- Bus 1 ---")
bus1 = BusSign(5)
for i in range(7):
    bus1.enter()

bus1.leave()
bus1.enter()

for i in range(6):
    bus1.leave()


print("\n--- Bus 2 ---")        
bus2 = BusSign(6, 3)
for i in range(10):
    bus2.enter()

bus2.leave()
bus2.enter()
bus2.all_leave()


print("\n--- Bus 3 ---")        
bus3 = BusSign(52, 8)
bus3.enter(40)
bus3.enter(21)
bus3.enter(20)
bus3.leave(7)
bus3.enter(5)
