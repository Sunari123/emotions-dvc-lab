import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/sample.csv")

def load_raw_dataset():
    df = pd.read_csv(DATA_PATH)
    return df

def split_features_label(df):
    X = df[["id"]].values
    y = df["value"].values
    return X, y