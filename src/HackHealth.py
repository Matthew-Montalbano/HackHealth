import pandas as pd
import NutritionalConstants
from fuzzywuzzy import fuzz


def add_item():
    is_correct_food = False
    while (not is_correct_food):
        food = input("What food would you like to add? ")
        actual_food = find_actual_food(food)
        is_correct_food = (input("Is this the correct food? Enter yes or no: ").lower() == 'yes')
    servings = int(input("How many servings did you have? "))
    food_nutrition_value = calculate_nutritional_information(actual_food, servings)
    track_data(food_nutrition_value)
    print(actual_food + " added!")

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
        todays_nutrition_count[index + 1] += nutrition_value
    tracking_data.iloc[-1] = todays_nutrition_count

def create_tracking_file():
    data = {"Day": [1],
            "Calories": [0],
            "Carb (g)": [0],
            "Fat (g)": [0],
            "Protein (g)": [0],
            "A": [0],
            "C": [0],
            "E": [0],
            "K": [0],
            "Sugar (g)": [0]
            }
    df = pd.DataFrame(data)
    df.to_excel("tracking.xlsx", index = False, encoding = "utf-8")
    return df

def create_new_row():
    new_row = {"Day": current_day,
               "Calories": 0,
               "Carb (g)": 0,
               "Fat (g)": 0,
               "Protein (g)": 0,
               "A": 0,
               "C": 0,
               "E": 0,
               "K": 0,
               "Sugar (g)": 0
               }
    return tracking_data.append(new_row, ignore_index=True)
    print(tracking_data)

food_data = pd.read_excel("food_data.xlsx")
try:
    tracking_data = pd.read_excel("tracking.xlsx")
except FileNotFoundError:
    tracking_data = create_tracking_file()

current_day = tracking_data.iloc[-1][0]

while (True):
    print("Please select an option:")
    print("A. List all available foods.")
    print("B. Add additional item to today.")
    print("C. See current status.")
    print("D. Save and advance to next day.")
    print("Q. Terminate program.\n")
    answer = input("Selection: ").lower()
    print()

    if answer == 'a':
        for index, name in enumerate(food_data['Food']):
            print(name)
    elif answer == 'b':
        add_item()
    elif answer == 'c':
        break
    elif answer == 'd':
        current_day += 1
        tracking_data = create_new_row()
        tracking_data.to_excel("tracking.xlsx", index = False, encoding = "utf-8")
        print("Day advanced to " + str(current_day) + ".")
    elif answer == 'q':
        break
    else:
        print("Invalid command. Please enter another.")
    print()
