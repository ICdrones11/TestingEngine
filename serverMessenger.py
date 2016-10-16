#!/usr/bin/python
# Wrapper around the REST API

import urllib2

class ServerMessenger:
    def __init__(self):
        self.serverAddress = "129.31.239.208:5000" # Hardcoded server address.
    
    def get(self):
        return 0
 #       urllib2.urlopen(self.serverAddress).read()


#s = Sender()

#print s.get()
