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
from langdetect import detect

print("Lyric pre-processor start ...")

# Set variables
dataset = []
flag = False
count = 0

# Stemmer initialize
porter = PorterStemmer()

# milestone count
mlc = 0
milestone = 20000

# Open csv file and fill dataset list
print("  ! Start preprocessing of dataset ...")
with open("lyrics.csv", "rt", encoding="utf8") as csvfile:
    wsreader = csv.reader(csvfile, delimiter=',')
    for row in wsreader:
        if flag:
            # Lower case -> replace new lines with space -> remove special characters -> stem
            lyric = porter.stem(((row[5].lower())).replace("\n", " ").translate({ord(i): None for i in "-_():#%&/*\"!?.\',"}))
                
            # language detection
            try:
                lang = detect(lyric)
            except:
                continue                
                
            stop_lang = "english"
            
            if (lang == "es"):
                stop_lang = "spanish"
            elif (lang == "it"):
                stop_lang = "italian"
            elif (lang == "fr"):
                stop_lang = "french"
            elif (lang == "de"):
                stop_lang = "german"
                
            stop_words = set(stopwords.words(stop_lang))
            if (stop_lang == "english"):
                stop_words.add("im")
                stop_words.add("i'm")
                stop_words.add("i am")
            
            # Tokenize on space characters and remove stop words
            lyric_tokens = lyric.split(" ")            
            
            filtered_lyric = [] 
            for w in lyric_tokens: 
                if w not in stop_words: 
                    filtered_lyric.append(w)
                    
            filtered_lyric = " ".join(filtered_lyric) # Join array of strings with space
            row[5] = re.sub(' +', ' ', filtered_lyric) # Remove multiple occurances of space with regex
            dataset.append(row)
            if(mlc % milestone == 0):
                print("Milestone reach: " + str(mlc / milestone))
            mlc += 1
            
        else:
            flag = True 
            
# Clean up for helping the csv process below
del flag, row, count, filtered_lyric, lyric, lyric_tokens, mlc, milestone

print("  ! Completed preprocessed dataset generation.")
print("  ! Writing to .csv file ...")

# Write the 2D dataset to a new .csv file
with open("lyrics_preproc.csv", 'w+', newline='', encoding="utf8") as new_csv:
    csvWriter = csv.writer(new_csv, delimiter=',')
    csvWriter.writerows(dataset)
    
print("  ! End of writing to .csv file.")
print("End of lyric pre-processor")



    
