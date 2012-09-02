from datetime import datetime
import sys

import urllib2

#import tweepy
sys.path.insert(0, 'libs/tweepy.zip')
from tweepy import *

BASE_URL = "0.0.0.0"

def get_messages_from_user(user, page=0):
    api = API()
    messages = api.user_timeline(user_id=user,count=200, page=page)
    print "Fetching page:" + str(page)

    ##### THis forces one page only    
    return messages

    if len(messages) > 0:
      return messages + get_messages_from_user(user,page+1)
    else:
      return messages 

def get_id_to_crawl():
    #### dfect
    return "1981171"

    #### rockstartup1
    return "608629166"

    response = urllib2.urlopen('http://' + BASE_URL + '/get-number') 
    return reponse

def send_id(user_id,hit_30,hit_15,hit_10,hit_5,hit_3,hit_1,hit_i_30,hit_i_15,hit_i_10,hit_i_5,hit_i_3,hit_i_1):
    response = urllib2.urlopen('http://' + BASE_URL + '/set-info?user='+user_id+"&hit_30="+hit_30+"&hit_15="+ hit_15+"&hit_10="+ hit_10 +"&hit_5="+ hit_5 +"&hit_3="+ hit_3 +"&hit_1="+ hit_1 +"&hit_i_30="+ hit_i_30 +"&hit_i_15="+ hit_i_15 +"&hit_i_10="+i hit_i_10 +"&hit_i_5="+ hit_i_5 +"&hit_i_3="+ hit_i_3 +"&hit_i_1=" + hit_i_1) 
    return

def check_for_hit(time_delta_minutes, target_message, messages):
    for message in messages:
        ## Message is now the user message that if is within the time range and with the client, is a hit
        if target_message[0] == message.source:
            message_time = datetime.strptime(message.created_at,"%Y-%m-%d %H:%M:%S")
            timedelta = abs((target_message[1] - message_time).total_seconds())
            hit_timedelta = time_delta_minutes * 60
            if timedelta < hit_timedelta:
                return True
    return False 

#  print message.source
#  print message.created_at

# Wake up, read rockstartuo file
file = open( "foo", "r" )
rockstartup = []
while 1:
    index = file.readline()
    if not index:
        break
    client = file.readline()
    message_time = datetime.strptime(file.readline(), "%Y-%m-%d %H:%M:%S")
    rockstartup.append([client,message_time]) 

while 1:
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

    for rockstartup_message in rockstarup:
        ### For each message, we check if we have any message that is <5,5>,<3,3>,<1,1>
        if check_for_hit(30,rockstartup_message,messages):
            hit_30 = hit_30 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_30 = hit_i_30 + 1
 
        if check_for_hit(15,rockstartup_message,messages):
            hit_15 = hit_15 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_15 = hit_i_15 + 1
 
        if check_for_hit(10,rockstartup_message,messages):
            hit_10 = hit_10 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_10 = hit_i_10 + 1
 
        if check_for_hit(5,rockstartup_message,messages):
            hit_5 = hit_5 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_5 = hit_i_5 + 1
 
        if check_for_hit(3,rockstartup_message,messages):
            hit_3 = hit_3 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_3 = hit_i_3 + 1
 
        if check_for_hit(1,rockstartup_message,messages):
            hit_1 = hit_1 + 1
            if rockstartup_message == "Twitter for iPad":
                hit_i_1 = hit_i_1 + 1
       
    send_id(id_to_crawl,hit_30,hit_15,hit_10,hit_5,hit_3,hit_1,hit_i_30,hit_i_15,hit_i_10,hit_i_5,hit_i_3,hit_i_1)
    break
