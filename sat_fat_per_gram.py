import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

food = pd.read_csv("nutrients_csvfile.csv")
type(food)

# Trace amounts of nutrients were denoted with a t, replacing that with 0.
food = food.replace("t", 0)
food = food.replace("t'", 0)

# Removing the comma from the strings so that I can convert to decimals.
food = food.replace(",", "", regex = True)

# Converting String objects to floating point decimals.
food['Grams'] = pd.to_numeric(food['Grams'], errors='coerce')
food['Calories'] = pd.to_numeric(food['Calories'], errors='coerce')
food['Protein'] = pd.to_numeric(food['Protein'], errors='coerce')
food['Fat'] = pd.to_numeric(food['Fat'], errors='coerce')
food['Sat.Fat'] = pd.to_numeric(food['Sat.Fat'], errors='coerce')
food['Fiber'] = pd.to_numeric(food['Fiber'], errors='coerce')
food['Carbs'] = pd.to_numeric(food['Carbs'], errors='coerce')

# Creating a unique list of categories.
categories = pd.unique(food['Category'])

# Main function
def main():

    choose_category()

# Handles a user choosing a category
def choose_category():

    choice = 'wrong'

    # Ensures the user can never pass an incorrect category
    while choice not in categories:
        for i in categories:
            print(f"{i}")
        if choice not in categories and choice != "wrong":
            choice = input
        elif choice == "wrong":
            choice = input("Type a category from the list above: ")
        if choice in categories:
            macro_check(choice)
            graph_builder(choice)

def macro_check(category):

    # Filtering my table based upon the Category
    filtered_food_table = food.where(food['Category'] == category)

    # Filtering based upon the ratio of fat to protein
    filtered_food_table['Ratio'] = filtered_food_table['Protein'] - filtered_food_table['Fat']
    low_fat = filtered_food_table.nlargest(n=10, columns=['Ratio'])

    print(low_fat[['Food', 'Measure', 'Calories', 'Protein', 'Fat', 'Carbs']])

# Builds the graph and takes a category as a paremeter
def graph_builder(category):

    converted_food = food

    # Calculating Protein, Calories and Fat per Gram
    protein_per_gram = round((converted_food['Protein'] / converted_food['Grams']), 2)
    fat_per_gram = round((converted_food['Fat'] / converted_food['Grams']), 2)
    carbs_per_gram = round((converted_food['Carbs'] / converted_food['Grams']), 2)
    calories_per_gram = round((converted_food['Calories'] / converted_food['Grams']), 2)

    # Setting Fat, Protein and Calories to their new per gram values
    converted_food['Fat'] = fat_per_gram
    converted_food['Protein'] = protein_per_gram
    converted_food['Carbs'] = carbs_per_gram
    converted_food['Calories'] = calories_per_gram

    # Filtering my table based upon the Category
    filtered_food = converted_food.where(converted_food['Category'] == category)

    # Filtering based upon the ratio of fat to protein
    filtered_food['Ratio'] = filtered_food['Protein'] - filtered_food['Fat']
    low_fat = filtered_food.nlargest(n=10, columns=['Ratio'])

    # Setting up my variables to use within the graph
    x = (low_fat['Food'])
    protein = np.array(low_fat['Protein'])
    fat = np.array(low_fat['Fat'])
    carbs = np.array(low_fat['Carbs'])

    # Plotting the graph
    plot.bar(x, protein, label = 'Protein')
    plot.bar(x, fat, bottom=protein, label = 'Fat')
    plot.bar(x, carbs, bottom=protein+fat, label='Carbs')

    # Setting all visual cues
    plot.xlabel("Food")
    plot.ylabel("Grams")
    plot.xticks(rotation=70)

    plot.legend(loc=1)

    plot.tight_layout()

    plot.show()

if __name__ == "__main__":
    main()