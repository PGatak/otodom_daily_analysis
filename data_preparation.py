import matplotlib.pyplot as plt
import pandas as pd
import warnings
import os


warnings.filterwarnings('ignore')
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

DATA_DIR = os.path.expanduser("~/scraping-data/otodom")
DIAGRAMS_DATA_DIR = os.path.expanduser("~/projects/flask_my_page/static/scraping-data/otodom/")
os.makedirs(DIAGRAMS_DATA_DIR, exist_ok=True)

# DATA PREPARATION
SELECTED_LOCATIONS = ['LSM', 'Czuby', 'Bronowice', 'Felin', 'Wrotków', 'Węglinek', 'Śródmieście', 'Czechów']
SELECTED_METERS = 80
SELECTED_PRICE = 850000
SELECTED_ROOMS = 4
dir_id = os.path.expanduser("~/scraping-data/otodom/data")
df = pd.read_csv((dir_id + '/results.csv'), usecols=['meters', 'price', 'rooms', 'dealer', 'district'], na_values=['Zapytajocenę', 'EMPTY', '>10'])
df = df.dropna()
df['rooms'].astype(int)

df = df[df['meters'] <= SELECTED_METERS][df['price'] <= SELECTED_PRICE][df['rooms'] <= SELECTED_ROOMS]
df = df[df['district'].isin(SELECTED_LOCATIONS)]

df['price_m2'] = round(df['price'] / df['meters']).astype(int)
describe = df.describe()
del df['price']

df['meters'] = round(df.meters).astype(int)
df['rooms'] = df.rooms.astype(int)


total_quantity_in_the_district = df['district'].value_counts()
