
import time
import random
import urllib2

random.seed()

while True:
    time.sleep(1)
    req = urllib2.Request('http://dfectuoso.com/')
    response = urllib2.urlopen(req)
    the_page = response.read()    

