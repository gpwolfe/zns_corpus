#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:24:37 2020

@author: piper
"""


from make_site_text_to_df import *

zns = site_text('https://znsbahamas.com/cuban-nationals-apprehended-in-bahamian-waters/')

zns.get_text()

zns.remove_text('akismet', 'processed') ## enter 'y' or 'n' to proceed

print(zns.text)

from corpus_dataframes.py import *

corpus = visible_corpus(zns.text)

bag = bag_of_words(corpus.lemma, corpus.tag)

no_stops = remove_stops(corpus)

bag_no_stops = bag_of_words(no_stops['lemma'], no_stops['tag'])

