#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:09:08 2019

@author: lakshmanteja
"""

import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords

import urllib.request
ISRO = urllib.request.urlopen('https://en.wikipedia.org/wiki/Bioinformatics')
html = ISRO.read()

from bs4 import BeautifulSoup
BS = BeautifulSoup(html, 'html5lib')
webtext = BS.get_text(strip=True)

word_tokens = [text for text in webtext.split()]


clean_tokens = word_tokens[:]
for token in word_tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
       
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)