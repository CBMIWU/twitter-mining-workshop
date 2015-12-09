#######################################################################################
# step3-plot-hashtag.py                                                               #
#                                                                                     #
# Purpose:  Twitter Mining Workshop. Plots the hashtag frequency from csv file        #
#            created in step 2                                                        #
# Python:  2.7 and up                                                                 #
# INPUT:	provide value for csvfile variable  in line 21                            #
# OUTPUT:	bar plot of hashtag frequency in png file                                 #
# AUTHOR:	Dajun Tian                                                                #
# TITLE:	Bioinformatics Assistant                                                  #
# ORGANIZATION:	Center for Biomedical Informatics, Washington University in St. Louis #
# DATE LAST UPDATED: 	12/7/2015                                                     #
# ATTRIBUTIONS: packages - matplotlib, numpy.   									  #
#######################################################################################

import csv
import numpy as np
import matplotlib.pyplot as plt

#use the csv file from step 2
with open('twitter_download-track.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    hashtag_list = []
	
	#it would be helpful to open the csv file first
	#hasttag is the 4th column in the csv file
    for row in reader:
        hashtag_list += row[3].split(',')

#remove the first element which is the header line
hashtag_list_all = hashtag_list[1:]

#hashtag_list to store all the hash tags
hashtag_list = []
for tag in hashtag_list_all[:]:
    if tag.strip():
        hashtag_list.append(tag.lower())
#count the frequency of each tag
from collections import Counter
freqs = Counter(hashtag_list)

labels, values = zip(*freqs.most_common(10))
indexes = np.arange(len(labels))
width = 1

plt.barh(indexes, values, width)
plt.yticks(indexes + width * 0.5, labels)
plt.savefig('tag-bar.png')
