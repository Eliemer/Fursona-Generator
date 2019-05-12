import pandas as pd
import random

animals = pd.read_csv('big_animals.csv', header=None, names=['Scientific Names'])

# print(animals.head())
def getFursona():
    index = random.randint(0, animals.size - 1)
    return animals.iloc[index].values
