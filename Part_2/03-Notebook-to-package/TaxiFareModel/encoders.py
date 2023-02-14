import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class DistanceTransformer(BaseEstimator, TransformerMixin):
    """
        Computes the haversine distance between two GPS points.
        Returns a copy of the DataFrame X with only one column: 'distance'.
    """

    def __init__(self,
                 start_lat="pickup_latitude",
                 start_lon="pickup_longitude",
                 end_lat="dropoff_latitude",
                 end_lon="dropoff_longitude"):
        # A COMPPLETER
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
    
    def fit(self, X, y=None):
        # A COMPLETER
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_['distance'] = haversine_vectorized(X_,
                                              self.start_lat,
                                             self.start_lon,
                                             self.end_lat,
                                             self.end_lon)
        return X_[['distance']]

class TimeFeaturesEncoder(BaseEstimator, TransformerMixin):
    """
        Extracts the day of week (dow), the hour, the month and the year from a time column.
        Returns a copy of the DataFrame X with only four columns: 'dow', 'hour', 'month', 'year'.
    """

    def __init__(self, time_column = 'pickup_datetime'):
       # A COMPLETER
        self.time_column = time_column

    def fit(self, X, y=None):
        # A COMPLETER
        return self

    def transform(self, X, y=None):
        # A COMPLETER 
        X_ = X.copy()
        X_[self.time_column] = pd.to_datetime(X_[self.time_column])
        X_['day_of_week'] = X_[self.time_column].dt.dayofweek
        X_['hour'] = X_[self.time_column].dt.hour
        X_['month'] = X_[self.time_column].dt.month
        X_['year'] = X_[self.time_column].dt.year
        return X_[['day_of_week', 'hour', 'month', 'year']]

def haversine_vectorized(df, 
                         start_lat="pickup_latitude",
                         start_lon="pickup_longitude",
                         end_lat="dropoff_latitude",
                         end_lon="dropoff_longitude"):
    """ 
        Calculates the great circle distance between two points 
        on the earth (specified in decimal degrees).
        Vectorized version of the haversine distance for pandas df.
        Computes the distance in kms.
    """

    lat_1_rad, lon_1_rad = np.radians(df[start_lat].astype(float)), np.radians(df[start_lon].astype(float))
    lat_2_rad, lon_2_rad = np.radians(df[end_lat].astype(float)), np.radians(df[end_lon].astype(float))
    dlon = lon_2_rad - lon_1_rad
    dlat = lat_2_rad - lat_1_rad

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat_1_rad) * np.cos(lat_2_rad) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return 6371 * c