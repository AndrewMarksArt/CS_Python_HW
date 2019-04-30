#
# hw5pr2.py ~ rps string analysis
#
# Name(s): Andrew Marks
#

import csv

def open_csv( filename="rps.csv" ):
   """ opens the file with name filename
         by default:  it looks for "rps.csv"
       reads all of the csv data and assembles it into
       a list-of-lists and then returns that...
       (Here, it uses the variable name LoL.
        Remember you can use any variable name!)
   """
   f = open(filename, newline='')
   reader = csv.reader(f)

   LoL = []
   for row in reader:
       LoL.append( row )

   # print("LoL is", LoL)
   f.close()

   return LoL


def score_string( rps ):
    """
    Takes in a single string rsp
    :param rps:
    :return: returns the count of the number of times the selected string occurs in the string rsp
    """
    rr_count = rps.count('rrs')
    return rr_count



if True:
   """ run functions/code here... """
   LoL = open_csv()  # uses the default filename


for i in range(len(LoL)):
    rps_to_score = LoL[i][2]
    score = score_string(rps_to_score)
    print(score)

"""
I ran the program over and over trying different features to count/test and then copied them to the results.csv file
from there I analyized the different features before deciding which was best and changing the labels to human or computer.
"""
