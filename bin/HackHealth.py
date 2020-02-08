import pandas as pd
import NutritionalConstants
from fuzzywuzzy import fuzz

food_data = pd.read_excel("food_data.xlsx")
tracking_data = pd.read_excel("tracking.xlsx")

def track_data():
    tracking_df = pd.read_excel('tracking.xlsx')

def find_actual_food(food_input):
    scores = []
    maximum = -1
    for index, food_actual in enumerate(food_data['Food']):
        scores[index] = (food_actual, fuzz.ratio[food_input, food_actual])
    for score in scores:
        if score[1] > maximum:
            maximum = score
            result = score[0]
    return result

def calculate_nutritional_information(food, servings):
    nutritional_information = food_data.loc[food_data['Food'] == food].loc[0]
    for index, nutrition in enumerate(nutritional_information):
        nutritional_information[index] = nutrition * servings
    return nutritional_information

def add_item():
    food = input("What food would you like to add? ")
    actual_food = find_actual_food(food)
    print(actual_food + " added!")


while (True):
    print("Please select an option:")
    print("A. List all available foods.")
    print("B. Add additional item to today.")
    print("C. See current status.")
    print("D. Advance to next day.")
    print("Q. Terminate program.\n")
    answer = input("Selection: ").lower()
    print()

    if answer == 'a':
        for index, name in enumerate(food_data['Food']):
            print(name)
        print()
    elif answer == 'b':
        add_item()
    elif answer == 'c':
        break
    elif answer == 'd':
        break
    elif answer == 'q':
        break
    else:
        print("Invalid command. Please enter another.\n")
