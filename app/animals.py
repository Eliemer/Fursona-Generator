import pandas as pd
import random

animals = pd.read_csv('big_animal.csv', index_col=0 , header=None, names=['Scientific Names'])

# print(animals.head())
def getFursona():
    index = random.randint(0, animals.size - 1)
    return animals.iloc[index].values
