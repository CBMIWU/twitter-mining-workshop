#######################################################################################
# step1-track-twitter.py                                                              #
#                                                                                     #
# Purpose:  Twitter Mining Workshop. Gets tweets by keyword (track=...)               #
# Python:  2.7 and up                                                                 #
# INPUT:	provide values for 4 Twitter credentials                                  #
# OUTPUT:	json file with tweets                                                     #
# AUTHOR:	Dajun Tian                                                                #
# TITLE:	Bioinformatics Assistant                                                  #
# ORGANIZATION:	Center for Biomedical Informatics, Washington University in St. Louis #
# DATE LAST UPDATED: 	12/7/2015                                                     #
# ATTRIBUTIONS: packages - Twython.   												  #
#######################################################################################

from twython import TwythonStreamer

import json

#the key, secret, token, token_secret were from the twitter developer site
API_KEY = "your API_KEY"
API_SECRET = "your API_SECRET"
OAUTH_TOKEN = "your OAUTH_TOKEN"
OAUTH_TOKEN_SECRET = "your OAUTH_TOKEN_SECRET"
#this the lat and log of MO
box_mo = '-95.774429, 35.904160, -89.098747, 40.613628'

class MyStreamer(TwythonStreamer):
    def __init__(self, out_file, maximum, *args):
        super(MyStreamer, self).__init__(*args)
        self.out_file = out_file
        self._count = 0
        #stores the maximum number of tweets to be downloaded
        self._maximum = maximum

    def on_success(self, data):
        if 'text' in data:
            self._count += 1
			#store the data to out_file
            json.dump(data, self.out_file)
            self.out_file.write('\n')
			#if the maximum reached, stop the download
			if self._count >= self._maximum:
                self.disconnect()
                print self._count, "tweets have been downloaded"

    def on_error(self):
        self.disconnect()

# open connection to a json/txt file
# open stream connection to twitter using credentials, and maximum values
# save incoming tweets to stream variable		
with open("twitter_download-track.json", 'w') as out_file:
    stream = MyStreamer(out_file, 100, API_KEY, API_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    print "file stored:", stream.out_file
    stream.statuses.filter(language='en', track=['health', 'healthy'])
