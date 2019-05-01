# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:56:41 2019

@author: UmutBerk
"""

# dataset link: https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics

import csv
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
import re

print("Lyric pre-processor start ...")

# Set variables
dataset = []
flag = False
count = 0

# Stemmer initialize
porter = PorterStemmer()

# Stop words initialize
stop_words = set(stopwords.words('english')) 
stop_words.add("you")
stop_words.add("I")
stop_words.add("im")
stop_words.add("I'm")
stop_words.add("i'm")
stop_words.add("i")

# Open csv file and fill dataset list
print("  ! Start preprocessing of dataset ...")
with open("lyrics.csv", "rt", encoding="utf8") as csvfile:
    wsreader = csv.reader(csvfile, delimiter=',')
    for row in wsreader:
        if flag:
            # Lower case -> replace new llines with space -> remove special characters
            lyric = porter.stem(((row[5].lower())).replace("\n", " ").translate({ord(i): None for i in "#%&/*\"!?.\',"}))
                                 
            # Tokenize on space characters and remove stop words
            lyric_tokens = lyric.split(" ")            
            
            filtered_lyric = [] 
            for w in lyric_tokens: 
                if w not in stop_words: 
                    filtered_lyric.append(w)
                    
            filtered_lyric = " ".join(filtered_lyric) # Join array of strings with space
            row[5] = re.sub(' +', ' ', filtered_lyric) # Remove multiple occurances of space with regex
            dataset.append(row)
        else:
            flag = True 
            
# Clean up for helping the csv process below
del flag, row, count, filtered_lyric, lyric, lyric_tokens, 

print("  ! Completed preprocessed dataset generation.")
print("  ! Writing to .csv file ...")

# Write the 2D dataset to a new .csv file
with open("lyrics_preproc.csv", "w+", encoding="utf8") as new_csv:
    csvWriter = csv.writer(new_csv, delimiter=',')
    csvWriter.writerows(dataset)
    
print("  ! End of writing to .csv file.")
print("End of lyric pre-processor")



    

