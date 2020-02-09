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
    df = pd.DataFrame(data).astype('float64')
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
    return tracking_data.append(new_row, ignore_index=True).astype('float64')
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
        print("Current Status:")
        print("-------------------------------------")
        print("Calories: " + str(tracking_data.iloc[-1][1]))
        print("Carbohydrates (g): " + str(tracking_data.iloc[-1][2]))
        print("Fat (g): " + str(tracking_data.iloc[-1][3]))
        print("Protein (g): " + str(tracking_data.iloc[-1][4]))
        print("Vitamin A: " + str(tracking_data.iloc[-1][5]))
        print("Vitamin C: " + str(tracking_data.iloc[-1][6]))
        print("Vitamin E: " + str(tracking_data.iloc[-1][7]))
        print("Vitamin K: " + str(tracking_data.iloc[-1][8]))
        print("Sugar (g): " + str(tracking_data.iloc[-1][9]))
        print("\nWarnings:")
        print("-------------------------------------")
        if (NutritionalConstants.CALORIES - tracking_data.iloc[-1][1] > 500):
            print("CALORIE DEFICIENCY BY " + str(NutritionalConstants.CALORIES - tracking_data.iloc[-1][1]))
        elif (NutritionalConstants.CALORIES - tracking_data.iloc[-1][1] < -500):
            print("CALORIE EXCESS BY " + str(tracking_data.iloc[-1][1] - NutritionalConstants.CALORIES))
        if (NutritionalConstants.CARBOHYDRATES - tracking_data.iloc[-1][2] > 33):
            print("CARBOHYDRATE DEFICIENCY BY " + str(NutritionalConstants.CARBOHYDRATES - tracking_data.iloc[-1][2]) + "g")
        elif (NutritionalConstants.CARBOHYDRATES - tracking_data.iloc[-1][2] < -33):
            print("CARBOHYDRATE EXCESS BY " + str(tracking_data.iloc[-1][2] - NutritionalConstants.CARBOHYDRATES) + "g")
        if (NutritionalConstants.TOTAL_FAT - tracking_data.iloc[-1][3] > 15):
            print("TOTAL FAT DEFICIENCY BY " + str(NutritionalConstants.TOTAL_FAT - tracking_data.iloc[-1][3]) + "g")
        elif (NutritionalConstants.TOTAL_FAT - tracking_data.iloc[-1][3] < -15):
            print("TOTAL FAT EXCESS BY " + str(tracking_data.iloc[-1][3] - NutritionalConstants.TOTAL_FAT) + "g")
        if (NutritionalConstants.PROTEIN - tracking_data.iloc[-1][4] > 14):
            print("PROTEIN DEFICIENCY BY " + str(NutritionalConstants.PROTEIN - tracking_data.iloc[-1][4]) + "g")
        elif (NutritionalConstants.PROTEIN - tracking_data.iloc[-1][4] < -14):
            print("PROTEIN EXCESS BY " + str(tracking_data.iloc[-1][4] - NutritionalConstants.PROTEIN) + "g")
        if (NutritionalConstants.VITAMIN_A - tracking_data.iloc[-1][5] > 25):
            print("VITAMIN A DEFICIENCY BY " + str(NutritionalConstants.VITAMIN_A - tracking_data.iloc[-1][5]) + "%")
        elif (NutritionalConstants.VITAMIN_A - tracking_data.iloc[-1][5] < -25):
            print("VITAMIN A EXCESS BY " + str(tracking_data.iloc[-1][5] - NutritionalConstants.VITAMIN_A) + "%")
        if (NutritionalConstants.VITAMIN_C - tracking_data.iloc[-1][6] > 25):
            print("VITAMIN C DEFICIENCY BY " + str(NutritionalConstants.VITAMIN_C - tracking_data.iloc[-1][6]) + "%")
        elif (NutritionalConstants.VITAMIN_C - tracking_data.iloc[-1][6] < -25):
            print("VITAMIN C EXCESS BY " + str(tracking_data.iloc[-1][6] - NutritionalConstants.VITAMIN_C) + "%")
        if (NutritionalConstants.VITAMIN_E - tracking_data.iloc[-1][7] > 25):
            print("VITAMIN E DEFICIENCY BY " + str(NutritionalConstants.VITAMIN_E - tracking_data.iloc[-1][7]) + "%")
        elif (NutritionalConstants.VITAMIN_E - tracking_data.iloc[-1][7] < -25):
            print("VITAMIN E EXCESS BY " + str(tracking_data.iloc[-1][7] - NutritionalConstants.VITAMIN_E) + "%")
        if (NutritionalConstants.VITAMIN_K - tracking_data.iloc[-1][8] > 25):
            print("VITAMIN K DEFICIENCY BY " + str(NutritionalConstants.VITAMIN_K - tracking_data.iloc[-1][8]) + "%")
        elif (NutritionalConstants.VITAMIN_K - tracking_data.iloc[-1][8] < -25):
            print("VITAMIN K EXCESS BY " + str(tracking_data.iloc[-1][8] - NutritionalConstants.VITAMIN_K) + "%")
        if (NutritionalConstants.SUGAR - tracking_data.iloc[-1][9] > 10):
            print("SUGAR DEFICIENCY BY " + str(NutritionalConstants.SUGAR - tracking_data.iloc[-1][9]) + "g")
        elif (NutritionalConstants.SUGAR - tracking_data.iloc[-1][9] < -10):
            print("SUGAR EXCESS BY " + str(tracking_data.iloc[-1][9] - NutritionalConstants.SUGAR) + "g")
    elif answer == 'd':
        current_day += 1
        tracking_data = create_new_row()
        tracking_data.to_excel("tracking.xlsx", index = False, encoding = "utf-8")
        print("Day advanced to " + str(current_day) + ".")
    elif answer == 'q':
        tracking_data.to_excel("tracking.xlsx", index = False, encoding = "utf-8")
        break
    else:
        print("Invalid command. Please enter another.")
    print()
