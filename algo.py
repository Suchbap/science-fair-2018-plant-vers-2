# python code for the alogorithm

import random
import sys
import os


plant = input("What is your plant type?: ")
location = input("Where are your plants located?")
mois = int(input("What is the soil moisture percentage?Please write the number: "))
temp = int(input("What is the temperature in degrees?: "))
fcast = input("What is the upcoming forecast- is it going to be rainy, sunny, or cloudy?: ")
if plant in ["beans","citrus", "cotton", "groundnut", "maize", "sorghum", "soybeans", "sunflower"]:
    if plant in "cotton" and mois >= 700 and mois <= 800:
        if temp > 60 and fcast in "sunny":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "cloudy":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "cotton" and mois > 800:
        if temp > 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "cotton" and mois < 700:
        if temp > 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    elif plant in "maize" and mois >= 500 and mois <= 550:
        if temp > 60 and fcast in "sunny":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "cloudy":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "maize" and mois > 550:
        if temp > 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "maize" and mois < 500:
        if temp > 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "soybeans" and mois >= 450 and mois <= 500:
        if temp > 60 and fcast in "sunny":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "cloudy":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "soybeans" and mois > 500:
        if temp > 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "soybeans" and mois < 450:
        if temp > 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")











