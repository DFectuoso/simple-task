
import time
import random
import urllib2

random.seed()

while True:
    for i in xrange(5):
        n = random.random()
        time.sleep(n)
    req = urllib2.Request('http://requestb.in/tg7qo0tg')
    response = urllib2.urlopen(req)
    the_page = response.read()    

