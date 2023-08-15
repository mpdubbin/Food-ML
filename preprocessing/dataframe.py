import pandas as pd


def fulfillment_center_info():
    """
    Function put the fulfillment center data into a pandas dataframe
    """
    df = pd.read_csv("data/fulfilment_center_info.csv")
    return df


def meal_info():
    """
    Function put the meal info data into a pandas dataframe
    """
    df = pd.read_csv("data/meal_info.csv")
    return df


def sample_submission():
    """
    Function put the sample submission data into a pandas dataframe
    """
    df = pd.read_csv("data/sample_submission.csv")
    return df


def test_data():
    """
    Function put the test data into a pandas dataframe
    """
    df = pd.read_csv("data/test.csv")
    return df


def train_data():
    """
    Function put the training data into a pandas dataframe
    """
    df = pd.read_csv("data/train.csv")
    return df