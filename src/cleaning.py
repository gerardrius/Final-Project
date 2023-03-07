import pandas as pd
import geopy.distance
import numpy as np

def trip_distance (df):
    distance = []

    for index, row in df.iterrows():
        lat0 = row['start_lat']
        lng0 = row['start_lng']
        lat1 = row['end_lat']
        lng1 = row['end_lng']
        try:
            distance.append(geopy.distance.distance((lat0, lng0), (lat1, lng1)).m)
        except:
            distance.append(np.nan)
            
    df['distance'] = distance
    
    return df