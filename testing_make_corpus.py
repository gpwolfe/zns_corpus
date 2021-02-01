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

from corpus_dataframes import *

full_text = visible_corpus(zns.text)

bow = bag_of_words(full_text.lemma, full_text.tag)

no_stops = remove_stops(full_text)

bow_no_stops = bag_of_words(no_stops['lemma'], no_stops['tag'])


# ways of handling the various parts of the corpus?
# making a dict of DataFrames?

corpus_dict = {'full_text': full_text, 'word_count': bow, 
                   'text_stops_removed': no_stops,
                   'word_count_stops_removed': bow_no_stops}




