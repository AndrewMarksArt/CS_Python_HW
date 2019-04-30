#
#
# titanic.py
#
# Andrew Marks

import numpy as np
from sklearn import datasets
import pandas as pd


try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")


# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('titanic6.csv', header=0)
df.head()
df.info()

# let's drop columns with too few values or that won't be meaningful
# Here's an example of dropping the 'body' column, column M
df = df.drop('body', axis=1)  # axis = 1 indicates we want to drop a column, not a row

# let's drop all of the rows with missing data:
df = df.dropna()

# careful!  You will need to drop more columns before dropping all of the N/A data!

# let's see our dataframe again...
# after some data-wrangling, I ended up with 1001 rows (anything over 500-600 seems reasonable)
df.head()
df.info()



# You'll need conversion to numeric datatypes for all input columns
#   Here's one example
#
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column

# let's see our dataframe again...
df.head()
df.info()


# you may need others!


print("+++ end of pandas +++\n")

# import sys
# sys.exit(0)

# separate into input X and target y dataframes...
X_all_df = df.drop('survived', axis=1)        # everything except the 'survival' column
y_all_df = df[ 'survived' ]                   # the target is survival! 

print("+++ start of numpy/scikit-learn +++")



#
# Use iris4.py as your guide - it's mostly copy-and-paste
# BUT -- there are points where things diverge...
# AND -- the goal is that you understand and feel more and more comfortable
#        with each of the parts of "the machine learning pipeline" ... !
#



#
# Note: for the Titanic data, it's the first 42 passengers who are unlabeled
#





"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how high were you able to get the average cross-validation (testing) score?



Then, include the predicted survival of the unlabeled data (in the original order).
We'll share the known results next week... :-)





"""