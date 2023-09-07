import numpy as np
import pandas as pd


def get_data(id):
    """
    generate random dataframe ignore id
    """
    return pd.DataFrame(np.random.random((100, 100)))

def worker(i, pipe):
    df = get_data(i)
    pipe.send(df.groupby(by=df.columns).sum())