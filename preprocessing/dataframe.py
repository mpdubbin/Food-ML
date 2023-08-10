import pandas as pd


def dataframe():
    df = pd.read_csv("data/CAERS_ASCII_2004_2017Q2.csv")
    return df