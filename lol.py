#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urllib2
import urlparse

home = "http://twitter.com/lol_o_clock"

links_url = "http://www.b3ta.com/links/popular/"
homemade_url = "http://www.b3ta.com/links/popular/?i=1" # b3tan's own
url = homemade_url

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

posts = soup.findAll('div',attrs={'class':['post1','post2']})
post=posts[0]
A = post.findAll('a')

burl = urlparse.urljoin(url,A[1]['href'])
sburl = urlparse.urljoin(url,A[-1]['href'])
link = A[2]['href']
title = A[2].string

if post.find(attrs={'class':'imadethis'}):
  link = sburl

import bitly
bcreds= open('bitly_creds').readlines()
blogin = bcreds[0].strip()
bapikey = bcreds[1].strip()
bapi = bitly.Api(login=blogin,apikey=bapikey)
slink = bapi.shorten(link)

tweet = "%s %s" % (title,link)
if len(tweet) > 140:
	tweet = "%s %s" % (title,link)

print home
print tweet
print len(tweet)
from twitter import Twitter, NoAuth, OAuth, read_token_file
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET
import os.path

oauth = OAuth(*read_token_file('twitter_oauth') + (CONSUMER_KEY, CONSUMER_SECRET))
twitter = Twitter(domain='api.twitter.com',auth=oauth, api_version='1')
twitter.statuses.update(status=tweet)
