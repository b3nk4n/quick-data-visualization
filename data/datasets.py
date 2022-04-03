import pandas as pd

__planet_headers = ['Planet', 'R (km)', 'mass (x 10^29 kg)']
__planet_data = [
    ['Mercury', 2440, 330.1],
    ['Venus', 6052, 4867.0],
    ['Earth', 6371, 5973.6],
    ['Moon', 1737, 73.5],
    ['Mars', 3390, 641.85]
]


def get_list_headers():
    return __planet_headers


def get_list(with_headers=False):
    if with_headers:
        return [__planet_headers] + __planet_data
    return __planet_data


def get_dataframe():
    return pd.read_csv('data/structured.csv', header=0)


def get_numpy_array():
    df = pd.read_csv('data/timeseries.csv', header=0)
    return df.to_numpy()
