#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:40:58 2021

@author: piper
"""

import spacy



nlp = spacy.load('/Users/piper/opt/anaconda3/envs/py3/lib/python3.8/site-packages/en_core_web_md/en_core_web_md-2.3.1')


def visible_corpus(text):
    """
    Creates a readable corpus in pandas DataFrame format using the
    readable string representations of a SpaCy Doc object.

    Parameters
    ----------
    text : string
        Preprocessed site text in a single string.

    Returns
    -------
    Pandas DataFrame with the following features: token, lemma, 
    simple POS ("tag"), detailed POS, and is_stop, indicating whether the 
    token is a stop-word.

    """
    doc = nlp(text)
        
    literals = [token.text for token in doc]
    lemmas = [token.lemma_ for token in doc]
    pos = [token.pos_ for token in doc]
    tags = [token.tag_ for token in doc]
    is_stop = [token.is_stop for token in doc]
    
    data = pd.DataFrame({'token': literals,'lemma':lemmas,'pos':pos,
                         'tag':tags, 'is_stop':is_stop})
    
    return data

def remove_stops(dataframe):
    """
    Removes stopwords from the mini-corpus returned by visible_corpus

    Parameters
    ----------
    dataframe : Pandas DataFrame
        Pass the dataFrame returned from visible_corpus.

    Returns
    -------
    Pandas DataFrame with tokens, lemmas, simple POS, detailed POS ("tag").
    Stopwords and the is_stop column are removed.

    """
    no_stops = dataframe[['token','lemma','pos','tag']][dataframe['is_stop'] == False]
    return no_stops
    
    
    
    
    

def bag_of_words(lemmas, tags):
    """
    Create a bag-of-words with unique lemma-POS combinations and their counts.

    Parameters
    ----------
    lemmas : pandas Series
        Series from DataFrame created by visible_corpus.
    tags : pandas Series
        Series from DataFrame created by visible_corpus.

    Returns
    -------
    Pandas DataFrame of unique lemmas, their detailed POS and their counts.

    """
    
    bow = pd.DataFrame({'lemma': lemmas, 'tag': tags})
    grouped_bow = bow.value_counts(sort=False)
    return grouped_bow



