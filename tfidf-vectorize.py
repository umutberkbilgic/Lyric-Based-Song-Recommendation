# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:32:13 2019

@author: UmutBerk
"""

# dataset link: https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics

import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

print("start ...")

# Set variables
dataset = []
vect = TfidfVectorizer(min_df=1)
count = 0
div = 10
top = 10
offset = 0
offset_counter = 0

print("  - Start reading csv file ...")
# Open csv file and fill dataset list
with open("lyrics_preproc.csv", "rt", encoding="utf8") as csvfile:
    wsreader = csv.reader(csvfile, delimiter=',')
    for row in wsreader:
        if (offset_counter >= offset):
            if(count % div == 0):
                dataset.append(row[5])
            count += 1
        else:
            offset_counter += 1
            
print("  - End reading csv file.")
            
print("    - TF-IDF matrix begin ...")
tfidf = vect.fit_transform(dataset)
arr = (tfidf * tfidf.T).A
print("    - TF-IDF matrix end.")    

# user select index and threshold
index = int(input("Enter index: "))
thres = float(input("Enter threshold: "))
simarr_sims = []
simarr_indexes = []
c = 0

# get all songs with tf-idf > set threshold
pray = np.array(arr[index])
for val in pray:
    if val >= thres:
        simarr_sims.append(val)
        simarr_indexes.append(c)
    c += 1
        
# report findings
for i in range(0, len(simarr_sims)):
    print("Song#" + str(i) + ": " + format(simarr_sims[i], '.4f') + " dataset index: " + str(simarr_indexes[i]))

print("End.")



    
