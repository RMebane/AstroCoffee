#!/usr/bin/env python
# -*- coding: utf-8 -*-

from astroph import preprint

import json
import requests

paper = preprint()

url = 'http://aasnova.org/2016/04/06/the-birth-of-super-earths-and-super-puffs/'

# Use Instaparser to parse the article
ip_api_key = 'b4a72359c1ba49569df55a9ccfcc1390'

ip_params = {'api_key': ip_api_key, 'url': url}

ip_response = requests.get('https://www.instaparser.com/api/1/article', params=ip_params)

ip_data = json.loads(ip_response.text)

# print(ip_response.url)
# print(ip_response.status_code)
# print(ip_data)
# print(ip_data['title'])
# print(ip_data['author'])
# print(ip_data['description'].encode("utf-8"))

paper.url = url
paper.title = ip_data['title'].encode("utf-8")
paper.errors = "0"
paper.numauth = 1
paper.author = ip_data['author'].encode("utf-8")
paper.abstract = ip_data['description'].encode("utf-8")
paper.date = 'Web Article:'
paper.sources = ''
paper.subject = ''
paper.comments = ''

print paper

# paper.url = url
# # Remove all the muck that screws up the BeautifulSoup parser
# # Will fail on PDF submission, so take care of that exception first
# try:
#     fhtml =re.sub(re.compile("<!--.*?-->", re.DOTALL), "", html)
#     soup = BeautifulSoup(fhtml)
#     paper.errors = "0"
# except:
#     paper.errors = "1"
#     paper.title = "Error Grabbing Title"
#     paper.author = "Error Grabbing Authors"
#     paper.numauth = "1"
#     paper.date = "Error Grabbing Date"
#     paper.abstract = "Error Grabbing Abstract"
#     paper.sources = " "
#     paper.subject = "Error Grabbing Subject"
#     paper.comments = "Error Grabbing Comments"
#     return paper
#
# # Grab the Title from the title tag
# try:
#     paper.title = soup.head.title.string
# except:
#     paper.errors = 1
#     paper.title = 'Error Grabbing Title'
#
# paper.numauth = 1
# paper.date = 'Web Article:'
# paper.author = ''
# paper.abstract = ''
# paper.sources = ''
# paper.subject = ''
# paper.comments = ''

# print(paper)
# return paper
