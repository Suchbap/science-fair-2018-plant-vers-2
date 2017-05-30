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
    if plant in "cotton" and mois >= 4.5 and mois <= 6.5:# Yuvanshu I checked the moisture percentages and we were way off adjusting now
        if temp > 60 and fcast in "sunny":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "cloudy":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "cotton" and mois > 10:
        if temp > 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "cotton" and mois <4.5 :
        if temp > 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    elif plant in "maize" and mois >= 20 and mois <= 25:#for mature corn
        if temp > 60 and fcast in "sunny":
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "cloudy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "maize" and mois >26:
        if temp > 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "rainy", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "maize" and mois < 20 and >=15:
        if temp > 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp > 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in ["sunny", "cloudy"]:
            print("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
        elif temp <= 60 and fcast in "rainy":
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
    if plant in "maize" and mois< 15:
            print ("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture percentage is",mois, "%.")
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

if plant in "corn" and mois<500 and >300:
if temp >=80 and fcast in ["sunny","cloudy"]:
         print("Your " + plant + " plant located in the " + location + "  needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif temp < 60 and fcast in["rainy", "Cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif temp <60 and fcast in"sunny":
            print ("Your " + plant + " plant located in the " + location + "doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.") if plant in "corn" and mois >=500 and fcast in ["sunny","rainy","cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif temp >=60 and <80 and mois<=300 and fcast in["rainy", "Cloudy"]:
            print("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif temp <60 and mois<=300 and fcast in"sunny":
            print ("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif temp <=60 and mois <=200 and fcast in "cloudy": 
            print ("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
    if plant in "wheat" and mois=>350 and <=500:
    if temp>60 and <80 and fcast in "cloudy":
            print ("Your " + plant + " plant located in the " + location + "  doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif mois>500 and fcast in["cloudy","rainy"]:
            print ("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif mois >=200 and <=300 and temp >60 and fcast in "sunny":
            print ("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif mois<300 and >250 and fcast in "rainy":
            print ("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")
        elif mois <250:
            print ("Your " + plant + " plant located in the " + location + " needs water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.") 
        elif mois >800:
            print ("Your " + plant + " plant located in the " + location + " doesn't need water since the temperature is",temp,"degrees Fahrenheit, the weather forecast is " + fcast + " and the soil moisture is",mois, "ml.")











