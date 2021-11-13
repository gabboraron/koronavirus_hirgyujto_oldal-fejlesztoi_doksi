#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php')
response_data = requestpost.json()
print(html.unescape(response_data["news"][0]))
currentNews = json.loads(response_data["news"][0])
print(html.unescape(currentNews["title"]))
print(html.unescape(currentNews["description"]))
print(html.unescape(currentNews["link"]))
print(requestpost.status_code)
