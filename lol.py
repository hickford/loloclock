#!/usr/bin/python
import os.path
import requests
import twitter
import twitter.cmdline
from bs4 import BeautifulSoup

home = "http://twitter.com/lol_o_clock"
print(home)

links_url = "http://www.b3ta.com/links/popular/"
homemade_url = "http://www.b3ta.com/links/popular/?i=1" # b3tan's own

oauth = twitter.OAuth(*twitter.read_token_file(os.path.expanduser('~/.twitter_oauth')) + (twitter.cmdline.CONSUMER_KEY, twitter.cmdline.CONSUMER_SECRET))
bird = twitter.Twitter(domain='api.twitter.com',auth=oauth, api_version='1.1')

def tweet(message):
    bird.statuses.update(status=message)

for url in [homemade_url]:
    response = requests.get(url)
    response.raise_for_status()
    page = response.content
    soup = BeautifulSoup(page)

    posts = soup.findAll('div',attrs={'class':['post1','post2']})

    for post in posts:
        anchors = post.findAll('a')
        anchor = anchors[2]

        link = anchor['href']
        title = anchor.string

        link = link or sburl      
        message = "%s %s" % (title,link)
        
        print(message)
        tweet(message)
        break
