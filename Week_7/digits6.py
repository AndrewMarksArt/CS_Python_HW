#
#
# digits6.py
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
df = pd.read_csv('digits6.csv', header=0)
df.head()
df.info()

# Convert feature columns as needed...
# You may to define a function, to help out:
def transform(s):
    """ from number to string
    """
    return 'digit ' + str(s)
    
df['label'] = df['64'].map(transform)  # the label in column 64
print("+++ End of pandas +++\n")

# import sys
# sys.exit(0)

# separate the data into input X and target y dataframes...
X_all_df = df.drop('label', axis=1)        # everything except the 'label' column
y_all_df = df[ 'label' ]                   # the label is the target! 

print("+++ start of numpy/scikit-learn +++")

# The data is currently in pandas "dataframes," but needs to be in numpy arrays
# These next two lines convert two dataframes to numpy arrays (using .values)
X_all = X_all_df.values        # iloc == "integer locations" of rows/cols
y_all = y_all_df.values      # individually addressable columns (by name)


#
# Use iris4.py as your guide - it's "mostly" copy-and-paste
# HOWEVER -- there are points where things diverge...
# AND -- our goal is that you understand and feel more and more comfortable
#        with each of the parts of "the machine learning pipeline" ... !
#
# Also: for the digits data...
#     + the first 10 rows [0:10] are unlabeled AND have only partial data!
#     + the next 12 rows [10:22] are unlabeled but have full data... .

X_unlabeled_partial = X_all[0:10]
y_unlabeled_partial = y_all[0:10]

X_unlabeled = X_all[10:22]
y_unlabeled = y_all[10:22]

X_labeled_orig = X_all[22:]  # labeled data starts at index 9
y_labeled_orig = y_all[22:]  # labeled data starts at index 9


# we scramble the data - but _only_ the labeled data!
#
indices = np.random.permutation(len(y_labeled_orig))  # indices are a permutation

# we scramble both X and y with the same permutation
X_labeled = X_labeled_orig[indices]              # we apply the same permutation to each!
y_labeled = y_labeled_orig[indices]              # again...

#
# Feature engineering ~ start ~
#
#
# some labels, in case we want to use them...
#
print("Some labels for the graphical tree:")
tn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # tn = "target names"

#
# Feature engineering ~ end ~
#

#
# We separate into test data and training data ...
#    + We will train on the training data...
#    + We will test on the testing data and see how well we do!
#    + We don't have a separate validation set of rows; we plan to use cross-validation (below)
TEST_SIZE = 10
X_test = X_labeled[:TEST_SIZE]    # first few are for testing
y_test = y_labeled[:TEST_SIZE]

X_train = X_labeled[TEST_SIZE:]   # all the rest are for training
y_train = y_labeled[TEST_SIZE:]

#
# Create a kNN model and tune its parameters
# There is only one parameter, k, the number of neighbors considered...
#
from sklearn.neighbors import KNeighborsClassifier

for k in [1,3,5,7,9,11,15,21,32,42,51,71,91]:
    knn = KNeighborsClassifier(n_neighbors=k)   # here, k is the "k" in kNN
    cv_scores = cross_val_score( knn, X_train, y_train, cv=5 ) # cv is the number of splits
    av = cv_scores.mean()
    print('k = ', k, ' avg score = ', av)


best_k = 1

# this is a new model! line is where the full training data is used for the model
knn_train = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_train.fit(X_train, y_train)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_test)
print(predicted_labels)

# and here are the actual labels
print("and the actual labels are")
actual_labels = y_test
print(actual_labels)

print('-----------------------------------')

knn_all = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_all.fit(X_all, y_all)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_all.predict(X_labeled[10:22])
print(predicted_labels)

# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_labeled[10:22]
print(actual_labels)











"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how smoothly were you able to adapt from the iris dataset to here?
  + how high were you able to get the average cross-validation (testing) score?
  
  I chose a K of 1 since it consistently had the best score
  relatively smoothly but I know I'm doing something wrong and its very hard to figure out where 
  the issues us when you have us copy and paste. It would be much better if you asked us to do something
  more generic so if we run into issues we can google to get help easier.



Then, include the predicted labels of the 12 full-data digits with no label
Past those labels (just labels) here:

You'll have 12 digit labels:

The predicted outputs are
['digit 0' 'digit 3' 'digit 1' 'digit 7' 'digit 4' 'digit 2' 'digit 4'
 'digit 1' 'digit 9' 'digit 5' 'digit 6' 'digit 2']
and the actual labels are
['digit 0' 'digit 3' 'digit 1' 'digit 7' 'digit 4' 'digit 2' 'digit 4'
 'digit 1' 'digit 9' 'digit 5' 'digit 6' 'digit 2']


And, include the predicted labels of the 10 digits that are "partially erased" and have no label:
Mention briefly how you handled this situation!?

Only use the top half to train your code. Do not train it using the bottom half.
This one had a lower testing-data score but both of them often had a 1.0 training-data score.

Past those labels (just labels) here:
You'll have 10 lines:






If you predicted the pixels themselves, cool! Share those, as well. (This is Ex. Cr.)


"""









#
# feature display - use %matplotlib to make this work smoothly
#


def show_digit( Pixels ):
    """ input Pixels should be an np.array of 64 integers (valued between 0 to 15) 
        there's no return value, but this should show an image of that 
        digit in an 8x8 pixel square
        Be sure to run
           %matplotlib
        at your ipython prompt before using this!
    """
    from matplotlib import pyplot as plt
    print(Pixels.shape)
    Patch = Pixels.reshape((8,8))
    plt.figure(1, figsize=(4,4))
    plt.imshow(Patch, cmap=plt.cm.gray_r, interpolation='nearest')  # plt.cm.gray_r   # plt.cm.hot
    plt.show()
    
# try it!
if False:
    row = 9 + 22
    Pixels = X_all[row:row+1,:]
    #show_digit(Pixels)
    print("That image has the label:", y_all[row])

# another try
if False:
    row = 5 + 22
    Pixels = X_all[row:row+1,:]
    #show_digit(Pixels)
    print("That image has the label:", y_all[row])


