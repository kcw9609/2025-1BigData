Exercise: Grouping and Sorting
This notebook is an exercise in the Pandas course. You can reference the tutorial at this link.

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")
Setup complete.
add Codeadd Markdown
Exercises
add Codeadd Markdown

1.
Who are the most common wine reviewers in the dataset? Create a Series whose index is the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote.

add Codeadd Markdown
# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').size()

# Check your answer
q1.check()
Correct:

reviews_written = reviews.groupby('taster_twitter_handle').size()
or

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
add Codeadd Markdown
#q1.hint()
#q1.solution()
add Codeadd Markdown
2.
What is the best wine I can buy for a given amount of money? Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).

add Codeadd Markdown
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
add Codeadd Markdown
# Check your answer
q2.check()
Correct

add Codeadd Markdown
#q2.hint()
#q2.solution()
add Codeadd Markdown
3.
What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.

add Codeadd Markdown
price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max']).sort_index()

# Check your answer
q3.check()
Correct

add Codeadd Markdown
print(price_extremes)
              min    max
variety                 
Abouriou     15.0   75.0
Agiorgitiko  10.0   66.0
Aglianico     6.0  180.0
Aidani       27.0   27.0
Airen         8.0   10.0
...           ...    ...
Zinfandel     5.0  100.0
Zlahtina     13.0   16.0
Zweigelt      9.0   70.0
Çalkarası    19.0   19.0
Žilavka      15.0   15.0

[707 rows x 2 columns]
add Codeadd Markdown
#q3.hint()
#q3.solution()
add Codeadd Markdown
4.
What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).

add Codeadd Markdown
price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max']).sort_index()
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=[False, False]).copy()

# Check your answer
q4.check()
Correct

add Codeadd Markdown
print(price)
add Codeadd Markdown
#q4.hint()
#q4.solution()
add Codeadd Markdown
5.
Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the taster_name and points columns.

add Codeadd Markdown
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

# Check your answer
q5.check()
Correct

add Codeadd Markdown
#q5.hint()
#q5.solution()
add Codeadd Markdown
Are there significant differences in the average scores assigned by the various reviewers? Run the cell below to use the describe() method to see a summary of the range of values.

add Codeadd Markdown
reviewer_mean_ratings.describe()
add Codeadd Markdown
6.
What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs. For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.

add Codeadd Markdown
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

# Check your answer
q6.check()
Correct

add Codeadd Markdown
