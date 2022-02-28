#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:24:37 2020

@author: piper
"""


from soup_from_zns import *

zns = SiteText('https://znsbahamas.com/cuban-nationals-apprehended-in-bahamian-waters/')
zns_ma = SiteText('https://znsbahamas.com/w-h-o-and-jack-ma-foundation-donate-p-p-e-to-caricom-states/')


zns.get_raw_text()
zns.raw_text
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


raw = zns.get_text_raw()
raw_doc = nlp(raw)
sents = [sent for sent in raw_doc.sents]
svg = displacy.render(raw_doc, style='dep', page = True, jupyter=False,minify=True)

from pathlib import Path
output_path = "sentence_renders.svg"
with open(output_path, "w", encoding = 'utf-8') as f:
    f.write(svg)
    

sentences = ["This is an example.", "This is another one."]
for sent in sentences:
    doc = nlp(sent)
    svg = displacy.render(doc, style="dep", jupyter=False)
    file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
    output_path = Path( '/images/' + file_name).mkdir(parents=True, exist_ok=True)
    output_path.open("w", encoding="utf-8").write(svg)
    
    
    
    
    
    
    
    
    