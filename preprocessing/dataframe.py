import pandas as pd


def fulfillment_center_info():
    """
    Function to put the fulfillment center data into a pandas dataframe
    """
    df = pd.read_csv("data/forecast_data/fulfilment_center_info.csv")
    return df


def meal_info():
    """
    Function to put the meal info data into a pandas dataframe
    """
    df = pd.read_csv("data/forecast_data/meal_info.csv")
    return df


def sample_submission():
    """
    Function to put the sample submission data into a pandas dataframe
    """
    df = pd.read_csv("data/forecast_data/sample_submission.csv")
    return df


def test_data():
    """
    Function to put the test data into a pandas dataframe
    """
    df = pd.read_csv("data/forecast_data/test.csv")
    return df


def train_data():
    """
    Function to put the training data into a pandas dataframe
    """
    df = pd.read_csv("data/forecast_data/train.csv")
    return df

print(fulfillment_center_info())