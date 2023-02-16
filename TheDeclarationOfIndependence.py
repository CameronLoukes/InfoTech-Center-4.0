# Programmer: Cameron Loukes
# Date: 2/8/23
# Program: Weather System Updates

#Import Libraries here
import random

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


(vehicleResponseSystem())

# I will create a system that will change the indside car tempurater depending on the conditions outside (This will only activate if Snowing, Blizzard, Icy. Or Sinshine)
def temperatureGuage():
    if weatherAlert == "Snowing":
        print("\nDue to the forcast of",weatherAlert, " your air conditioning has been set to High")
    elif weatherAlert == "Blizzard":
        print("\nDue to the forcast of",weatherAlert, " your air conditioning has been set to High")
    elif weatherAlert == "Icy":
        print("\nDue to the forcast of",weatherAlert, " your air conditioning has been set to High and Defrost has been engaged")
    elif weatherAlert == "Sunshine":
        print("\nDue to the forcast of",weatherAlert, " your air conditiong has been set to cool")
    elif weatherAlert == "Windy":
        print("")
    elif weatherAlert == "Rainy":
        print("")
    else:
        print("")
        
(temperatureGuage())



