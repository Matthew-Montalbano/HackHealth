import pandas as pd
import NutritionalConstants
from fuzzywuzzy import fuzz

def find_actual_food(food_input):
    scores = []
    maximum = -1
    for index, food_actual in enumerate(food_data['Food']):
        scores.append((food_actual, fuzz.ratio(food_input, food_actual)))
    for score in scores:
        if score[1] > maximum:
            maximum = score[1]
            result = score[0]
    print('found food ' + result)
    return result

def calculate_nutritional_information(food, servings):
    nutritional_information = food_data.loc[food_data['Food'] == food].iloc[0][1:-1]
    for index, nutrition in enumerate(nutritional_information):
        nutritional_information[index] = nutrition * servings
    print('finished calculating nutritional info')
    return nutritional_information

def track_data(food_nutrition_value):
    todays_nutrition_count = tracking_data.iloc[-1]
    for index, nutrition_value in enumerate(food_nutrition_value):
        todays_nutrition_count[index] += nutrition_value
    tracking_data.iloc[-1] = todays_nutrition_count

def add_item():
    food = input("What food would you like to add? ")
    actual_food = find_actual_food(food)
    servings = int(input("How many servings did you have? "))
    food_nutrition_value = calculate_nutritional_information(actual_food, servings)
    track_data(food_nutrition_value)
    print(actual_food + " added!")

def create_tracking_file():
    data = {"calories": [0],
            "Carb (g)": [0],
            "Fat (g)": [0],
            "Protein(g)": [0],
            "A": [0],
            "C(mg)": [0],
            "E": [0],
            "K": [0],
            "sugar(g)": [0]
            }
    df = pd.DataFrame(data)
    df.to_excel("tracking.xlsx", index = False, encoding = "utf-8")
    return df


food_data = pd.read_excel("food_data.xlsx")
try:
    tracking_data = pd.read_excel("tracking.xlsx")
except FileNotFoundError:
    tracking_data = create_tracking_file()

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
