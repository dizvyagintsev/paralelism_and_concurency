from utils import get_data


def costly_operation(df):
    """
    Perform a costly operation on a dataframe.
    """
    return df.groupby(by=df.columns).sum()


df1 = get_data(1)

print(costly_operation(df1))

