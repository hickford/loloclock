#!python
from BeautifulSoup import BeautifulSoup
import urllib2
import urlparse

links_url = "http://www.b3ta.com/links/popular/"
homemade_url = "http://www.b3ta.com/links/popular/?i=1" # b3tan's own
url = links_url

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

tweet = "%s %s" % (title,link)
print tweet

