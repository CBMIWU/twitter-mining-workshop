#######################################################################################
# step2-tweets2csv.py                                                                 #
#                                                                                     #
# Purpose:  Twitter Mining Workshop. Saves tweets from json file into a csv file      #
# Python:  2.7 and up                                                                 #
# INPUT:	provide value for json and csv files                                      #
# OUTPUT:	csv file with tweets                                                      #
# AUTHOR:	Dajun Tian                                                                #
# TITLE:	Bioinformatics Assistant                                                  #
# ORGANIZATION:	Center for Biomedical Informatics, Washington University in St. Louis #
# DATE LAST UPDATED: 	12/7/2015                                                     #
#######################################################################################

import csv
import json
#json_file is the input file that contains the tweets downloaded
#csv_file is the file that will store the extracted fields from json_file
json_file = "twitter_download-track.json"
csv_file = "twitter_download-track.csv"

with open(json_file, 'r') as infile, open(csv_file, 'w') as outfile:
	#this defines the head of the csv file
    var_list = ["created_at", 'favorite_count', "retweet_count", 'hashtags', 'text']
	
    writer = csv.DictWriter(outfile, fieldnames = var_list, lineterminator = '\n')
    writer.writeheader()
    #loop through each line
    for line in infile:
        tweet_dict = {}
		#use try statement as sometimes there would be errors when downloading tweets
        try:
			#load each line from the input file into a python dictionary
            json_dict = json.loads(line)
			
			#repr is applied as some of the tweet contains non ASCII characters
            tweet_dict['text'] = repr(json_dict['text'])
            tweet_dict['favorite_count'] = json_dict['favorite_count']
            tweet_dict["retweet_count"]= json_dict["retweet_count"]
            tweet_dict["created_at"] = json_dict["created_at"]
			
			# hash tag is a list under this embedded dictionary
            hashtags = json_dict["entities"]["hashtags"]
            print hashtags
            hashtag_list = []
			
			#loop through the hash tag and join multiple hash tags by comma
            for tag in hashtags:
                hashtag_list.append(tag['text'].encode("utf8","ignore"))
            tweet_dict['hashtags'] = ','.join(hashtag_list)
        except:
			#if any of the variables were not find, all fields would be blank
            tweet_dict['text'] = None
            tweet_dict['favorite_count'] = None
            tweet_dict['hashtags'] = None
            tweet_dict["retweet_count"] = None
            tweet_dict["created_at"] = None
        #tweet_dict.pop('text', None)

        writer.writerow(tweet_dict)
    print "All tweets are converted to csv"
