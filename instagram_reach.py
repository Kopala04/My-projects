# This is one of the best choice to see how well your post reach. That helps us understand how instagram algorithm works
# and do best out of it.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

data = pd.read_csv('instagram data.csv', encoding = 'latin1')
# print(data.head())

# Let’s have a look at whether this dataset contains any null values or not:
data.isnull().sum()

# We know it has , so let's drop all those null values and move on
data.dropna()

# Let’s have a look at the insights of the columns to understand the data type of all the columns
data.info()

# Now we can start analyzing the reach of instagram posts from home.

# plt.figure(figsize=(10, 8))
# plt.style.use('fivethirtyeight')
# plt.title("Distribution of Impressions From Home")
# sns.displot(data['From Home']) # We could use distplot , but in seaborn version 0.14.0 it will be removed so now we are going to type displot.
# plt.show()


# Now we can check impressions from hashtags

# plt.figure(figsize=(10, 8))
# plt.title("Distribution of Impressions From Hashtags")
# sns.histplot(data['From Hashtags'])
# plt.show()

# Now let's see various different sources and their peaks.

# home = data["From Home"].sum()
# hashtags = data["From Hashtags"].sum()
# explore = data["From Explore"].sum()
# other = data["From Other"].sum()
#
# labels = ['From Home','From Hashtags','From Explore','Other']
# values = [home, hashtags, explore, other]
#
# fig = px.pie(data, values=values, names=labels,
#              title='Impressions on Instagram Posts From Various Sources', hole=0.5)
# fig.show()



