import pandas as pd

def get_data(nrows=10000):
    '''returns a DataFrame with nrows from s3 bucket'''
    # A COMPLETER
    df = pd.read_csv('path/to/file.csv', nrows=nrows)
    return df

def clean_data(df, test=False):
    '''returns a DataFrame without outliers and missing values'''
    # A COMPLETER
    df = df[(df['distance'] >= 0) & (df['distance'] <= 100)]
    df = df[(df['fare_amount'] >= 2.5) & (df['fare_amount'] <= 100)]
    df.dropna(inplace = True)
    if not test:
        df = df[df['fare_amount'] > 0]
    return df