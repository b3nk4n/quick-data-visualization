import pandas as pd

__planet_headers = ['Planet', 'R (km)', 'mass (x 10^29 kg)']
__planet_data = [
    ['Sun', 696000, 1989100000],
    ['Earth', 6371, 5973.6],
    ['Moon', 1737, 73.5],
    ['Mars', 3390, 641.85]
]


def get_list_with_headers(with_headers=False):
    if with_headers:
        return [__planet_headers] + __planet_data
    return __planet_data


def get_dataframe():
    return pd.read_csv('data/structured.csv', header=0)


def get_numpy_array():
    df = pd.read_csv('data/timeseries.csv', header=0)
    return df.to_numpy()
