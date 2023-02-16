# Programmer: Cameron Loukes
# Date: 1/23/23
# Program:

"""
I will create personalized driver settings for different drivers
"""

# Import Libraries Here:
import random
import time.sleep

def drivers():
    listOfDrivers = ["Driver 1", "Driver 2", "Driver 3", "Driver 4"]
    chooseDriver = random.choice(listOfDrivers)
    return drivers

def radio():
    listOfRadioStations = ["Top Hits", "Pop", "HipHop", "Rock", "Country", "Jazz"]
    chooseRadioStation = random.choice(listOfRadioStations)

def steeringWheel():
    listOfWheelPositions = ["Low", "Medium", "High"]
    chooseWheelPosition = random.choice(listOfWheelPositions)

def seat():
    listOfSeatPositions = ["Close", "Middle", "Far"]
    chooseSeatPosition = random.choice(listOfSeatPositions)

# Create settings for drivers

def driverSettings():
    if "Driver 1":
        print("Driver 1 has been chosen")
    elif "Driver 2":
    elif "Driver 3":
    else "Driver 4":
