# -*- coding: utf-8 -*-

#######################################################################################
# streaming twitter.py                                                                #
#                                                                                     #
# Purpose:  Twitter Mining Workshop. Maintains a connection to Twitter through a loop #
# Python:  2.7 and up                                                                 #
# INPUT:	provide values for 4 Twitter credentials                                  #
# OUTPUT:	json file with tweets                                                     #
# AUTHOR:	Dajun Tian                                                                #
# TITLE:	Bioinformatics Assistant                                                  #
# ORGANIZATION:	Center for Biomedical Informatics, Washington University in St. Louis #
# DATE LAST UPDATED: 	Nov 20 08:52:49 2014                                          #
# ATTRIBUTIONS: packages - Twython.   												  #
#######################################################################################

from twython import TwythonError, TwythonStreamer
import time
import json
import sys
from requests.exceptions import ChunkedEncodingError

API_KEY = "your API_KEY"
API_SECRET = "your API_SECRET"
OAUTH_TOKEN = "your OAUTH_TOKEN"
OAUTH_TOKEN_SECRET = "your OAUTH_TOKEN_SECRET"
bounding_box_mo = '-95.774429, 35.904160, -89.098747, 40.613628'

class MyStreamer(TwythonStreamer):
    
    def __init__(self, *args):
        print "init runs"
        super(MyStreamer, self).__init__(*args)
        self.out_file_path = "MO-geo-tagged-pulledFromTwitter-cbmi-" + \
                            time.strftime("%Y-%m-%dT%H-%M-%S", time.localtime()) + ".json"
        self.out_file = open(self.out_file_path, 'w')

    def on_success(self, data):
        if 'text' in data:
            json.dump(data, self.out_file)
            self.out_file.write('\n')
            
    def on_error(self, e):
        print "on_error:", e
        self.disconnect()
        self.out_file.close()
while True:
    try:
        stream = MyStreamer(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        print "file stored:", stream.out_file_path
        stream.statuses.filter(language='en', locations=bounding_box_mo)
        
    except ChunkedEncodingError as e:
        print "ChunkedEncodingError:", e
        stream.on_error(e)
        print "disconnected and sleep for 10 seconds"
        time.sleep(10)
    
    except TwythonError as e:
        print e
        stream.on_error(e)
        print "disconnected and sleep for 10 seconds"
        time.sleep(10)
        
    except KeyboardInterrupt as e:
        print "key error catched", e
        stream.on_error(e)
        print "disconnected and sleep for 10 seconds"
        time.sleep(10)
    except:
        print sys.exc_info()[0]
        stream.on_error(sys.exc_info()[0])
        time.sleep(10)