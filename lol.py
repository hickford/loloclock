#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
from six.moves.urllib_parse import urljoin
import os.path
home = "http://twitter.com/lol_o_clock"
print(home)

links_url = "http://www.b3ta.com/links/popular/"
homemade_url = "http://www.b3ta.com/links/popular/?i=1" # b3tan's own

import twitter
import twitter.cmdline

oauth = twitter.OAuth(*twitter.read_token_file(os.path.expanduser('~/.twitter_oauth')) + (twitter.cmdline.CONSUMER_KEY, twitter.cmdline.CONSUMER_SECRET))
bird = twitter.Twitter(domain='api.twitter.com',auth=oauth, api_version='1.1')

for url in [homemade_url,links_url]:
    response = requests.get(url)
    response.raise_for_status()
    page = response.content
    soup = BeautifulSoup(page)
    posts = soup.findAll('div',attrs={'class':['post1','post2']})

    for post in posts:
        A = post.findAll('a')

        burl = urljoin(url,A[1]['href'])
        sburl = urljoin(url,A[-1]['href'])
        link = A[2]['href']
        title = A[2].string

        if post.find(attrs={'class':'imadethis'}):
            link = sburl
            if url == links_url:
                continue            
             
        tweet = "%s %s" % (title,link)
        
        # broken
        if False and len(tweet) > 140:
            import bitly
            bcreds= open(os.path.expanduser('~/.bitly_creds')).readlines()
            blogin = bcreds[0].strip()
            bapikey = bcreds[1].strip()
            bapi = bitly.Api(login=blogin,apikey=bapikey)
            slink = bapi.shorten(link)
            tweet = "%s %s" % (title,slink)

        print(tweet)

        try:
            bird.statuses.update(status=tweet)
            break
        except twitter.api.TwitterHTTPError as E:
            print(E)
            continue
     