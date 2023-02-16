# Programmer: Cameron Loukes
# Date: 1/23/23
# Program:

"""
I will create personalized driver settings for different drivers
"""

# Import Libraries Here:
import random
from time import sleep

def drivers():
    listOfDrivers = ["Driver 1", "Driver 2", "Driver 3", "Driver 4"]
    chooseDriver = random.choice(listOfDrivers)
    return drivers

def radio():
    listOfRadioStations = ["Top Hits,", "Pop,", "HipHop,", "Rock,", "Country,", "Jazz,"]
    chooseRadioStation = random.choice(listOfRadioStations)

def steeringWheel():
    listOfWheelPositions = ["Low,", "Medium,", "High,"]
    chooseWheelPosition = random.choice(listOfWheelPositions)

def seat():
    listOfSeatPositions = ["Close", "Middle", "Far"]
    chooseSeatPosition = random.choice(listOfSeatPositions)

# Create settings for drivers

def driverSettings():
    if drivers == "Driver 1":
        print("Driver 1 has been chosen")
        sleep(2)
        print("Radio is beeing set to ",radio, " steering wheel is being set to ",steeringWheel, " and seat position is being set to",seat,)
    elif dirvers == "Driver 2":
        print("Driver 2 has been chosen")
        sleep(2)
        print("Radio is being set to ",radio, " steering wheel is being set to ",steeringWheel, " and seat position is being set to",seat,)
    elif drivers == "Driver 3":
        print("Driver 3 has been chosen")
        sleep(2)
        print("Radio is being set to ",radio, " steering wheel is being set to ",steeringWheel, " and seat position is being set to",seat,)
    else drivers == "Driver 4":
        print("Driver 4 has been chosen")
        sleep(2)
        print("Radio is being set to ",radio, " steering wheel is being set to ",steeringWheel, " and seat position is being set to",seat,)

        (driverSettings())