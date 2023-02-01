# Programmer: Cameron Loukes
# Date: 1/30/23
# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge level
   - Create a List with Gas Levels
   - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
   - Create a List of Gas Stations
   - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
   - Print Gas level
   - Print Closest Gas Station
"""

# Import Libraries Here
import random
from time import sleep

# Gas Level Function
def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable Calling gasLevelGauge Function to store its value
gasLevelIndicator = gasLevelGuage()

# Gas Station Function
def listOfGasStations():
   gasStations = ["Shell", "Speedway", "Costco", "BP", "Buc-ee's", "Ctigo", "Circle K", "Meijer"]
   closestGasStation = random.choice(gasStations)
   return closestGasStation

# Determine Gas Level & Closest Gas Station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25), 2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is low, checking Google Maps for the closest gas station")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away")

gasLevelAlert()