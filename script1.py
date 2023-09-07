from utils import get_data


def costly_operation(df):
    """
    Perform a costly operation on a dataframe.
    """
    return df.groupby(by=df.columns).sum()


df1 = get_data(1)
df2 = get_data(2)

print(costly_operation(df1))
print(costly_operation(df2))

