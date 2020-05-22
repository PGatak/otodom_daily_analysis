import matplotlib.pyplot as plt
import os
import seaborn as sns
from data_preparation import df, DIAGRAMS_DATA_DIR


plt.figure()
fig = plt.figure(figsize=(18, 6))
plt.subplot2grid((1, 3), (0, 0))
a1 = sns.distplot(df.meters)
plt.title("distribution: square meters")

plt.subplot2grid((1, 3), (0, 1))
a1 = sns.distplot(df.price_m2)
plt.title('distribution: price per square meter')

plt.subplot2grid((1, 3), (0, 2))
a1 = sns.distplot(df.rooms)
plt.title('distribution: number of rooms')
fig.savefig(os.path.join(DIAGRAMS_DATA_DIR, "distributions.png"))

#################################################################

facet = plt.figure(2)
facet = sns.FacetGrid(df, hue="rooms", aspect=4)
facet.map(sns.kdeplot, 'price_m2', shade= True)
facet.set(xlim=(0, df['price_m2'].max()))
facet.add_legend()
plt.grid()
plt.xlim(df.price_m2.min(), df.price_m2.max())
facet.savefig(os.path.join(DIAGRAMS_DATA_DIR, "rooms_price_m2.png"))

#################################################################

facet = plt.figure(2)
facet = sns.FacetGrid(df, hue="rooms",aspect=4)
facet.map(sns.kdeplot,'price_m2',shade= True)
facet.set(xlim=(0, df['price_m2'].max()))
facet.add_legend()
plt.title('average price per square meter divided into the number of rooms')
plt.grid()
plt.xlim(df.price_m2.min(), df.price_m2.max())
facet.savefig(os.path.join(DIAGRAMS_DATA_DIR, "rooms_price_m2.png"))

#################################################################

fig = plt.figure(4)
df["dealer"].value_counts().hist(bins=50)
plt.ylabel("number of sellers")
plt.xlabel("number of offers")
fig.savefig(os.path.join(DIAGRAMS_DATA_DIR, "sellers_offers.png"))

#################################################################

facet = plt.figure(5)
facet = sns.FacetGrid(df, hue="rooms",aspect=4)
facet.map(sns.kdeplot,'meters',shade= True)
facet.set(xlim=(18, df['meters'].max()))
plt.grid()
facet.add_legend()
plt.xlim(18, 80)
plt.title('average number of meters divided into the number of rooms')
facet.savefig(os.path.join(DIAGRAMS_DATA_DIR, "meters_rooms.png"))

#################################################################

facet = plt.figure(6)
facet = sns.FacetGrid(df, hue="district",aspect=4)
facet.map(sns.kdeplot,'price_m2',shade= True)
facet.set(xlim=(0, df['price_m2'].max()))
facet.add_legend()
plt.title('average price per square meter divided into districts')
plt.xlim(5200, 10000)
facet.savefig(os.path.join(DIAGRAMS_DATA_DIR, "price_m2_district.png"))

#################################################################
#################################################################
#################################################################
#################################################################