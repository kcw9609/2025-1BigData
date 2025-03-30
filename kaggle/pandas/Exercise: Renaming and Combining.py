Introduction
Run the following cell to load your data and some utility functions.

add Codeadd Markdown
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")
Setup complete.
add Codeadd Markdown
Exercises
View the first several lines of your data by running the cell below:

add Codeadd Markdown
1.
region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with these columns renamed to region and locale, respectively.

add Codeadd Markdown
# Your code here
renamed = reviews.rename(columns={'region_1' : 'region'}).rename(columns = {'region_2' : 'locale'})

# Check your answer
q1.check()
Correct

add Codeadd Markdown
#q1.hint()
q1.solution()
Solution:

renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))
add Codeadd Markdown
2.
Set the index name in the dataset to wines.

add Codeadd Markdown
reindexed = reviews.rename_axis("wines" , axis='columns')

# Check your answer
q2.check()
Correct

add Codeadd Markdown
#q2.hint()
#q2.solution()
add Codeadd Markdown
3.
The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.

add Codeadd Markdown
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
add Codeadd Markdown
Create a DataFrame of products mentioned on either subreddit.

add Codeadd Markdown
combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()
Correct

add Codeadd Markdown
#q3.hint()
#q3.solution()
add Codeadd Markdown
4.
The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:

add Codeadd Markdown
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
add Codeadd Markdown
Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. Using this, generate a dataset combining the two tables into one.

add Codeadd Markdown
left = powerlifting_meets.set_index('MeetID')
right = powerlifting_competitors.set_index('MeetID')

powerlifting_combined = left.join(right)
add Codeadd Markdown


# Check your answer
q4.check()
Correct

add Codeadd Markdown
#q4.hint()
q4.solution()
Solution:

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
add Codeadd Markdown
