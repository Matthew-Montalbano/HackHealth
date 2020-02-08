import pandas as pd
import Core
import NutritionalConstants


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


    
    def collect_data(self):
        enter_more = True
        while (enter_more):
            food_input = input("What food did you eat?")
            food_actual = self.find_actual_food(food_input)
            servings = input("How many servings did you eat?")

