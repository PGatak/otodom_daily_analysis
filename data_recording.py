import os
import json
from data_preparation import describe, total_quantity_in_the_district, df, DATA_DIR


#DATA_DIR = os.path.expanduser("~/scraping-data/otodom/aa")
os.makedirs(DATA_DIR, exist_ok=True)
districts_quantity_json = os.path.join(DATA_DIR, "districts_quantity.json")
describe_json = os.path.join(DATA_DIR, "describe.json")
rooms_value_count_json = os.path.join(DATA_DIR, "rooms_value_count.json")
groupby_json = os.path.join(DATA_DIR, "groupby.csv")
dealers_value_counts_json = os.path.join(DATA_DIR, "dealers_value_counts.csv")
groupby_number_of_offers_json = os.path.join(DATA_DIR, "groupby_number_of_offers.csv")


#################################################################
districts_quantity = {}
for district, quantity in total_quantity_in_the_district.items():
    districts_quantity[district] = {
        "district": district,
        "quantity": quantity
    }

#################################################################

rooms_value = df.rooms.value_counts()
rooms_value_count = {}
for rooms, value in rooms_value.items():
    rooms_value_count[rooms] = {
        "rooms": rooms,
        "value": value
    }
print(rooms_value_count)

#################################################################
count = describe.meters[0]
meters_min = describe.meters[3]
meters_25 = describe.meters[4]
meters_50 = describe.meters[5]
meters_75 = describe.meters[6]
price_mean = describe.price[1]
price_min = describe.price[3]
price_m2_mean = describe.price_m2[1]
price_m2_min = describe.price_m2[3]
price_m2_25 = describe.price_m2[4]
price_m2_50 = describe.price_m2[5]
price_m2_75 = describe.price_m2[6]
price_m2_max = describe.price_m2[7]

#################################################################

describe = {
    "count": count,
    "meters_min": meters_min,
    "meters_25": meters_25,
    "meters_50": meters_50,
    "meters_75": meters_75,
    "price_mean": round(price_mean),
    "price_min": price_min,
    "price_m2_min": price_m2_min,
    "price_m2_25": price_m2_25,
    "price_m2_50": price_m2_50,
    "price_m2_75": price_m2_75,
    "price_m2_max": price_m2_max

}

#################################################################

groupby = round(df['price_m2'].groupby([df['dealer'], df['district'], df['rooms']]).mean().to_frame())
groupby.to_csv(groupby_json)

#################################################################

dealers_value_counts = df["dealer"].value_counts()[0:20]
dealers_value_counts.to_csv(dealers_value_counts_json)

#################################################################
groupby_number_of_offers = df['district'].groupby([df['dealer'], df['district'], df['rooms']]).count()
groupby_number_of_offers.to_csv(groupby_number_of_offers_json)

#################################################################
with open(districts_quantity_json, "w+") as json_file:
    print("SAVING NEW REVERSE URLS", districts_quantity_json)
    json.dump(districts_quantity, json_file, indent=4)

with open(describe_json, "w+") as json_file:
    print("SAVING NEW REVERSE URLS", describe_json)
    json.dump(describe, json_file, indent=4)

with open(rooms_value_count_json, "w+") as json_file:
    print("SAVING NEW REVERSE URLS", rooms_value_count_json)
    json.dump(rooms_value_count, json_file, indent=4)
