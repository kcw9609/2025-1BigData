Introduction
Run the following cell to load your data and some utility functions.

add Codeadd Markdown
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")
Setup complete.
add Codeadd Markdown
Exercises
add Codeadd Markdown
1.
What is the data type of the points column in the dataset?

add Codeadd Markdown
# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()
Correct

add Codeadd Markdown
#q1.hint()
#q1.solution()
add Codeadd Markdown
2.
Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.

add Codeadd Markdown
point_strings = reviews.points.astype('str')

# Check your answer
q2.check()
Correct

add Codeadd Markdown
#q2.hint()
#q2.solution()
add Codeadd Markdown
3.
Sometimes the price column is null. How many reviews in the dataset are missing a price?

add Codeadd Markdown
n_missing_prices = reviews.loc[pd.isnull(reviews.price)].shape[0]

# Check your answer
q3.check()
Correct

add Codeadd Markdown
#q3.hint()
#q3.solution()
add Codeadd Markdown
4.
What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending order. Your output should look something like this:

Unknown                    21247
Napa Valley                 4480
                           ...  
Bardolino Superiore            1
Primitivo del Tarantino        1
Name: region_1, Length: 1230, dtype: int64
add Codeadd Markdown
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False) # 정답코드
add Codeadd Markdown
reviews_filled_Null = reviews.region_1.fillna('Unknown');
reviews_per_region = reviews_filled_Null.groupby(reviews_filled_Null).size().sort_values(ascending=False)
add Codeadd Markdown
## reviews.region_1.fillna('Unknown').groupby(reviews.region_1).size().sort_values(ascending=False)
## 오류코드 -> Unknown으로 채웠지만 groupby에서 원본을 사용
add Codeadd Markdown

# Check your answer
q4.check()
Correct

add Codeadd Markdown
#q4.hint()
#q4.solution()
add Codeadd Markdown
