import pandas as pd


def dataframe():
    """
    Function to read the kaggle csv into a dataframe; function so that the dataframe doesn't need to be stored and can be accessed in-memory.
    """
    df = pd.read_csv("data/CAERS_ASCII_2004_2017Q2.csv")
    return df