#
#
# digits6.py
# Name: Marie Boys & Monica Montano 
#

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

# that's it!
    
print("+++ End of pandas +++\n")

# import sys
# sys.exit(0)

# separate the data into input X and target y dataframes...
X_all_df = df.drop('64', axis=1)        # everything except the 'label' column
y_all_df = df[ '64' ]                   # the label is the target! 

print("+++ start of numpy/scikit-learn +++")

# The data is currently in pandas "dataframes," but needs to be in numpy arrays
# These next two lines convert two dataframes to numpy arrays (using .values)
X_all = X_all_df.values        # iloc == "integer locations" of rows/cols
y_all = y_all_df.values      # individually addressable columns (by name)

#
# Use iris6.py as your guide - it's "mostly" copy-and-paste
# HOWEVER -- there are points where things diverge...
# AND -- our goal is that you understand and feel more and more comfortable
#        with each of the parts of "the machine learning pipeline" ... !

## [0:10]
X_unlabeled = X_all[:10,:]
y_unlabeled = y_all[:10]

X_labeled_orig = X_all[:10,:] 
y_labeled_orig = y_all[:10]


## [10:22]
X_unlabeled = X_all[:10,:22]
y_unlabeled = y_all[:10:22]


X_labeled_orig = X_all[:10,:22]
y_labeled_orig = y_all[:10:22]


indices = np.random.permutation(len(y_labeled_orig))

X_labeled = X_labeled_orig[indices]              # we apply the same permutation to each!
y_labeled = y_labeled_orig[indices]


# Also: for the digits data...
#     + the first 10 rows [0:10] are unlabeled AND have only partial data!
#     + the next 12 rows [10:22] are unlabeled but have full data... .
#
# You should create TWO sets of unlabeled data to be predicted.
#     + extra credit:  predict the missing pixels themselves!


TEST_SIZE = 10
X_test = X_labeled[:TEST_SIZE]    # first few are for testing
y_test = y_labeled[:TEST_SIZE]

X_train = X_labeled[TEST_SIZE:]   # all the rest are for training
y_train = y_labeled[TEST_SIZE:]

# Create a kNN model and tune its parameters 
# There is only one parameter, k, the number of neighbors considered...
#
from sklearn.neighbors import KNeighborsClassifier

best_k = 0
best_av = 0

for k in range(1,101):   # not likely to be a good value...
    knn = KNeighborsClassifier(n_neighbors=k)   # here, k is the "k" in kNN

    #
    # cross-validation
    #
    # This runs a routine that splits only the training set into two pieces:
    # model-building and model-validation. We'll use "build" and "validate"
    #
best_k = 0
best_av = 0

for k in range(1,101):   # not likely to be a good value...
    knn = KNeighborsClassifier(n_neighbors=k)   # here, k is the "k" in kNN

    #
    # cross-validation
    #
    # This runs a routine that splits only the training set into two pieces:
    # model-building and model-validation. We'll use "build" and "validate"
    #
    cv_scores = cross_val_score( knn, X_train, y_train, cv=5 ) # cv is the number of splits
    # print('\nthe cv_scores are')
    # for s in cv_scores:
    #     # we format it nicely...
    #     s_string = "{0:>#7.4f}".format(s) # docs.python.org/3/library/string.html#formatexamples
    #     print("   ",s_string)
    av = cv_scores.mean()
    print(k , 'neighbors has average: ', av)

    if av > best_av:
      best_av = av
      best_k = k

    print("best_k is", best_k, "with av", best_av)

best_k = best_k


#
# this is a new model! line is where the full training data is used for the model
knn_train = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_train.fit(X_train, y_train)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_test)
print(predicted_labels)

# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_test
print(actual_labels)

# 
# let's do more formatted printing!
#

print("\n\n")

#
# formatted printing! (docs.python.org/3/library/string.html#formatstrings)

# the headers
s = "{0:<11} | {1:<11}".format("Predicted","Actual")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)

# the separators
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)

# here is the table...
for pi, ai in zip( predicted_labels, actual_labels ):
    # pi and ai are the index of the predicted and actual label
    plabel = tn[pi]  # tn is target_names - see above
    alabel = tn[ai]
    s = "{0:<11} | {1:<11}".format(plabel,alabel)
    print(s)

print("\n\n")

# 
# here is where you'll do the same thing -- but now for the unlabeled data!
#

# this is a new model! line is where the full training data is used for the model
knn_train = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_train.fit(X_labeled, y_labeled)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_test)
print(predicted_labels)

# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_test
print(actual_labels)

knn_train = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_train.fit(X_labeled, y_labeled)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_unlabeled,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_unlabeled)
print(predicted_labels)

# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_unlabeled
print(actual_labels)


#
#
#
#








"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how smoothly were you able to adapt from the iris dataset to here?
  + how high were you able to get the average cross-validation (testing) score?



Then, include the predicted labels of the 12 full-data digits with no label
Past those labels (just labels) here:

You'll have 12 digit labels:




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
if False:  # change False to True
    row = 24 - 2
    Pixels = X_all[row:row+1,:]
    show_digit(Pixels)
    print("That image has the label:", y_all[row])

# another try
if True:  # change False to True
    row = 28 - 2
    Pixels = X_all[row:row+1,:]
    #show_digit(Pixels)
    print("That image has the label:", y_all[row])


