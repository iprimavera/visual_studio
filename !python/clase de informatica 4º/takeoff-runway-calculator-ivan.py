unitPower = input("* what is the Unit Power: ")
weight = input("* what is the Weight: ")
unitPower = int(unitPower)
weight = int(weight)
hectometers = 0
speed = 0
while speed < 300:
    hectometers += 1
    speed = (( unitPower * 2 * hectometers ) / weight ) * 1.4
else:
    print("the runway must have", hectometers * 100, "meters")