# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:54:06 2024

@author: win
"""

import os
import sys
import urllib.request
client_id="9T8tE7mZUcjQelUjCn9S"
client_secret="rSxmfthmqM"
encText = urllib.parse.quote("AI")
url="https://openapi.naver.com/v1/search/blog?query=" + encText # JSON  RESULT
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response=urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body=response.read()
    print(response_body.decode('utf-8'))
else:
    print("ERROR CODE: "+ rescode)
    