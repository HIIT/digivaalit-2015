#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import sys, tweepy, datetime, getopt

from secrets import *

# Joku voi halutessaan siivota tätä

timeformat = "%Y-%m-%d"
maxdate = datetime.datetime.today()
mindate = datetime.datetime.today()
username = ""
oldest = 0
outputfile = "output.txt"
silent = False
final = []
# autentikaatiojuttu
auth = tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
auth.set_access_token(AccessTokenKey,AccessTokenSecret)
api = tweepy.API(auth)

def printHelp():
	print "Usage: %s --username [--output file.txt] [--silent] [--max date] [--min date] [--format] [--help] "
	print "\n"
	print "-u --username [username]"
	print "-m --max	[max. date]	default: today"
	print "-n --min	[min. date]	default: today"
	print "-f --format [date format]	default: %Y-%m-%d"
	print "-h --help"

def log(text):
	if silent != True:
		print text

opt, arg = getopt.getopt(sys.argv[1:], "hm:n:f:u:", ["help", "max", "min", "format","username"])

for o, a in opt:
	if o in ["-h","--help"]:
		printHelp()
		sys.exit(0)
	if o in ["-m", "--max"]:
		maxdate = datetime.datetime.strptime(a,timeformat)
	if o in ["-n", "--min"]:
		mindate = datetime.datetime.strptime(a,timeformat)
	if o in ["-f", "--format"]:
		timeformat = a
	if o in ["-u", "--username"]:
		username = a

if username == "":
	print "No username specified"
	sys.exit(2)

tweets = []

# get tweets
newtweets = api.user_timeline(screen_name=username, count=200)
tweets.extend(newtweets)
oldest = tweets[-1].id - 1

while len(newtweets) > 0:
	newtweets = api.user_timeline(screen_name=username, count=200, max_id=oldest)
	tweets.extend(newtweets)
	oldest = tweets[-1].id - 1

tweets = sorted(tweets, key=lambda x: x.created_at)
for tweet in tweets:
	twtime = tweet.created_at
	twid = tweet.id
	#print twtime.strftime(timeformat)
	#print twid

	if mindate <= twtime <= maxdate:
		print twtime.strftime(timeformat)+" "+tweet.text
