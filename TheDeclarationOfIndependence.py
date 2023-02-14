# Programmer: Cameron Loukes
# Date: 1/23/23
# Program: Infotech Center Upgrades
# Merged Welcome Screen and Gasoline Branches - Stable

"""
Our Welcome Screen will start our Program letting
drivers know that the Infotech Center 4.0 OS is loading
"""

#Import Libraries Here
import time  # I imported the time library for further use in code.
import sys  # I imported the system library for further use in code.
import random
from time import sleep

print('\n\033[1;36;40m Welcome to InfoTech Center 4.0')

x = 0
a = 0

time.sleep(2)
print('')

while x != 20:
    x += 1
    b = ("\033[1;33;40m Infotech Center 4.0 OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\033[1;32;40m Infotech Center 4.0 OS is Loaded!')

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
        print("\n***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("\n***Warning***")
        sleep(1)
        print("Your gas tank is low, checking Google Maps for the closest gas station")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("\n***WARNING***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank, "miles away")
    elif gasLevelIndicator == "Half Tank":
        print("\nYou are on Half a Tank which is plenty to make it to your destination")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("\nYou are on Three Quarters of a tank which is plenty to make it to your destination")
    else:
        print("\nYour Gas Tank is Full")




# Weather function

# Create weather conditions in a list and choose it randomly
def weather():
    weatherForcast = ["Snowing", "Blizzard", "Rainy","Foggy", "Windy", "Icy", "Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

#Variable to call weather() once in our VRS()
weatherAlert = weather()



#VRS() to respond to the weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehick to go 45MPH")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehick to go 35MPH")
    elif weatherAlert == "Rainy":
        print("\nNWS is calling for",weatherAlert,"conditions, drive safely")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert, "conditions, drive safely")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert, "conditions, drive safely")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your alarm by 40 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehick to go 25MPH")
    else:
        print("\nNWS is callig for",weatherAlert,"drive safely and have a nice day")






#Call Funtions Here
print("\nNational Weather Service is checking conditions...")
sleep(2)
vehicleResponseSystem()
print("\nChecking current gas levels...")
sleep(2)
gasLevelAlert()