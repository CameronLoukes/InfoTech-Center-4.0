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


# Gas Level Function
def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

print(gasLevelGuage())


# Gas Station Function
def listOfGasStations():
   gasStations = ["Shell", "Speedway", "Costco", "BP", "Buc-ee's", "Ctigo", "Circle K", "Meijer"]
   closestGasStation = random.choice(gasStations)
   return closestGasStation

print(listOfGasStations())
