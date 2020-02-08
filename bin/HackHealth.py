import pandas as pd
import NutritionalConstants
from fuzzywuzzy import fuzz

class HackHealth:

    def __init__(self):
        self.food_data = self.read_in_food_data()

    def read_in_food_data(self):
        df = pd.read_excel('food_data.xlsx')
        return df
    
    def track_data(self):
        tracking_df = pd.read_excel('tracking.xlsx')
    
    def find_actual_food(self, food_input):
        scores = []
        minimum = -1
        for index, food_actual in enumerate(self.food_data['Food']):
            scores[index] = (food_actual, Core.stringCompare[food_input, food_actual])
        for score in scores:
            if score[1] < minimum or score[1] == -1:
                minimum = score
                result = score[0]
        return result
    
    def calculate_nutritional_information(self, food, servings):
        nutritional_information = self.food_data.loc[self.food_data['Food'] == 'apple'].loc[0]
    
    while (True):
        print("Please select an option:")
        print("A. List all available foods.")
        print("B. Add additional item to today.")
        print("C. See current status.")
        print("D. Advance to next day.")
        print("Q. Terminate program.\n")
        answer = input("Selection: ").lower()

        if answer == 'a':
            break
        elif answer == 'b':
            break
        elif answer == 'c':
            break
        elif answer == 'd':
            break
        elif answer == 'q':
            break
        else:
            print("Invalid command. Please enter another.\n")
