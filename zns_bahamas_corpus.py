#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:25:30 2020

@author: piper
"""

from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import spacy
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

site = "https://znsbahamas.com/cuban-nationals-apprehended-in-bahamian-waters/"

site_html = requests.get(site)
site_soup = BeautifulSoup(site_html.content, 'html.parser').prettify()
site_soup.prettify()
all_ps = site_soup.find_all('p')
texts = [x.get_text() for x in site_soup('p')]
texts_together  = ' '.join(texts)
texts_together = re.sub(r'[^ \w]', '', texts_together).lower()
texts_together = re.sub(r' {2,5}', ' ', texts_together)
texts_together

# stopwords
stopwords = spacy.lang.en.stop_words.STOP_WORDS.add(' ')



# NOW use Spacy to tokenize the text
# because conda and spacy don't work well together, you have to 
# tell spacy EXACTLY WHERE TO LOOK for the tokenizer, rather than trying to import

nlp = spacy.load('/Users/piper/opt/anaconda3/envs/py3/lib/python3.8/site-packages/en_core_web_md/en_core_web_md-2.3.1')


tokenizer = Tokenizer(nlp.vocab)
tokens = tokenizer(texts_together)


# calling token.lemma_  (note the underscore) will return the lemmas. Otherwise
# lemma returns some numbers

doc = nlp(texts_together)

for token in doc:
    print(token.lemma_, token.pos_, token.tag_)
lemmas = [token.lemma_ for token in doc if not token.is_stop]
tags = [token.tag_ for token in doc if not token.is_stop]
pos = [token.pos_ for token in doc if not token.is_stop]

## Create pandas DataFrame from above

zns = pd.DataFrame({'lemma':lemmas,'tag':tags,'pos':pos})




















