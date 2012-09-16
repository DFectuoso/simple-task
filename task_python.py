#!/usr/bin/env python
import sys, time
from daemon import Daemon
import random

random.seed()

from datetime import datetime
import urllib2
sys.path.insert(0, 'libs/tweepy.zip')
from tweepy import *

BASE_URL = "ec2-174-129-124-24.compute-1.amazonaws.com"

rockstartup = []

def get_messages_from_user(user, page=0):
    api = API()
    print "Fetching user " + user
    try:  
      messages = api.user_timeline(user_id=user,count=200, page=page)
    except:
      print "We are on the limit, wait 15 secs, and call this again"
      time.sleep(15)
      return get_messages_from_user(user,page)

    print "Fetching page:" + str(page)
    #time.sleep(30)
    if len(messages) > 0:
      print "The last message of the user is from " + str(messages[-1].created_at)
      print "While the last rockstartup1 message is from: "+str(rockstartup[-1][1])
      if messages[-1].created_at > rockstartup[-1][1]:
        return messages + get_messages_from_user(user,page+1)
      else:
        return messages
    else:
      return messages 

def get_id_to_crawl():
    response = urllib2.urlopen('http://' + BASE_URL + '/get-number').read()
    print "Crawling " + str(response)
    foo = str(response).strip()
    print "foo|" + foo + "|foo"
    return foo

def send_id(user_id,hit_30,hit_15,hit_10,hit_5,hit_3,hit_1,hit_i_30,hit_i_15,hit_i_10,hit_i_5,hit_i_3,hit_i_1):
    response = urllib2.urlopen('http://' + BASE_URL + '/set-info?user='+user_id+"&hit_30="+str(hit_30)+"&hit_15="+ str(hit_15)+"&hit_10="+ str(hit_10) +"&hit_5="+ str(hit_5) +"&hit_3="+ str(hit_3) +"&hit_1="+ str(hit_1) +"&hit_i_30="+ str(hit_i_30) +"&hit_i_15="+ str(hit_i_15) +"&hit_i_10="+ str(hit_i_10) +"&hit_i_5="+ str(hit_i_5) +"&hit_i_3="+ str(hit_i_3) +"&hit_i_1=" + str(hit_i_1))
    return

def check_for_hit(time_delta_minutes, target_message, messages):
    for message in messages:
        ## Message is now the user message that if is within the time range and with the client, is a hit
        if target_message[0] == message.source:
            message_time = message.created_at
            timedelta = abs((target_message[1] - message_time).total_seconds())
            hit_timedelta = time_delta_minutes * 60
            if timedelta < hit_timedelta:
                return True
    return False 

#  print message.source
#  print message.created_at

# Wake up, read rockstartuo file
file = open( "foo", "r" )
while 1:
    index = file.readline()
    if not index:
        break
    client = file.readline().strip()
    foo = file.readline().strip()
    message_time = datetime.strptime(foo, "%Y-%m-%d %H:%M:%S")
    rockstartup.append([client,message_time]) 

print "Finish set up"

##class MyDaemon(Daemon):
##  def run(self):
while True:
  print "Here"
  hit_30 = 0
  hit_15 = 0
  hit_10 = 0
  hit_5 = 0
  hit_3 = 0
  hit_1 = 0
  hit_i_30 = 0
  hit_i_15 = 0
  hit_i_10 = 0
  hit_i_5 = 0
  hit_i_3 = 0
  hit_i_1 = 0
  # Ask for id
  id_to_crawl = get_id_to_crawl()
  if id_to_crawl == "FAIL": 
      break
  # Get all messages
  messages = get_messages_from_user(id_to_crawl)
  for rockstartup_message in rockstartup:
      ### For each message, we check if we have any message that is <5,5>,<3,3>,<1,1>
      if check_for_hit(30,rockstartup_message,messages):
          hit_30 = hit_30 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_30 = hit_i_30 + 1
      if check_for_hit(15,rockstartup_message,messages):
          hit_15 = hit_15 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_15 = hit_i_15 + 1
      if check_for_hit(10,rockstartup_message,messages):
          hit_10 = hit_10 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_10 = hit_i_10 + 1
      if check_for_hit(5,rockstartup_message,messages):
          hit_5 = hit_5 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_5 = hit_i_5 + 1
      if check_for_hit(3,rockstartup_message,messages):
          hit_3 = hit_3 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_3 = hit_i_3 + 1
      if check_for_hit(1,rockstartup_message,messages):
          hit_1 = hit_1 + 1
          if rockstartup_message[0] == "Twitter for iPad":
              hit_i_1 = hit_i_1 + 1
     
  print "About to send hits:"
  print "hit 30: " + str(hit_30) + " " + str(hit_i_30)
  print "hit 15: " + str(hit_15) + " " + str(hit_i_15)
  print "hit 10: " + str(hit_10) + " " + str(hit_i_10)
  print "hit 5: " + str(hit_5) + " " + str(hit_i_5)
  print "hit 3: " + str(hit_3) + " " + str(hit_i_3)
  print "hit 1: " + str(hit_1) + " " + str(hit_i_1)
  send_id(id_to_crawl,hit_30,hit_15,hit_10,hit_5,hit_3,hit_1,hit_i_30,hit_i_15,hit_i_10,hit_i_5,hit_i_3,hit_i_1)


#
#if __name__ == "__main__":
#  daemon = MyDaemon('/tmp/daemon-example.pid')
#  if len(sys.argv) == 2:
#    if 'start' == sys.argv[1]:
#      daemon.start()
#    elif 'stop' == sys.argv[1]:
#      daemon.stop()
#    elif 'restart' == sys.argv[1]:
#      daemon.restart()
#    else:
#      print "Unknown command"
#      sys.exit(2)
#    sys.exit(0)
#  else:
#    print "usage: %s start|stop|restart" % sys.argv[0]
#    sys.exit(2)
#
