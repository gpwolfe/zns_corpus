#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:05:00 2020

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


class InputError(Exception):
    pass
    



class site_text:
    """
    Pass site URL as a string
    """
    
    def __init__(self, site):
         self.site = site
         
         self.site_html = requests.get(self.site)
         self.site_soup = BeautifulSoup(self.site_html.content, 
                                        'html.parser').prettify()
    
    def get_text(self):
        """
        

        Parameters
        ----------
        site_soup : TYPE
            DESCRIPTION.

        Returns
        -------
        A list of words representing the text of the website.

        """
        
        
    
    def process(self, text):
        """
        Removes punctuation and extra spaces from the text and transforms all
        words to lowercase.
        
        Parameters
        ----------
        text : List
            A list of words from get_text. 


        Returns
        -------
        A string of all words in the list passed to the function, 
        each separated by one space.

        """
        texts_together = ' '.join(text)
        text_no_punct_lower = re.sub(r'[^ \w]', '', texts_together).lower()
        text_one_space = re.sub(r' +', ' ', text_no_punct_lower)
        return text_one_space
        
        
    
    def remove_text(self, text, beginning_cut, end_cut):
        """
        Uses regular expressions to match beginning_text and end_text. Deletes
        all text, starting with the first character of beginning_text, ending 
        with last character of end_text

        Parameters
        ----------
        text : string
            A string of text, such as the string returned from the function 
            'process'
        beginning_cut : string
            A unique string in the site text that is included in the text to
            be deleted.
        end_cut : string
            A string that appears after the beginning_text. Will be included
            in the deletion.

        Returns
        -------
        A string of text equivalent to the string passed, without the text 
        including and between 'beginning_cut' and 'end_cut'

        """
        # Check if beginning_cut and end_cut appear in text
        try: 
            front_split = text.split(beginning_cut)
        except: 
            InputError(f"\"{front_split}\" doesn't seem to be here. Please check your beginning cut and type it exactly as it appears in the text.")
        try:
            back_split = front_split[1].split(end_cut)
        except:
            InputError(f"\"{back_split}\" doesn't seem to appear after your beginning cut. Please check your end cut and type it exactly as it appears in the text.")
        # Check that beginning_cut and end_cut are unique          
        if len(front_split) > 2:
            raise InputError(f"\"{front_split}\" occurs more than once in the text. Try typing more words for your beginning cut.")
        if len(back_split) > 2:
            raise InputError(f"\"{back_split}\" occurs more than once in the text. Try typing more words for your end cut.")
        new_text = front_split[0] + back_split[1]
        return re.sub(r' +', ' ', new_text)
     
            
            
        

        
        
        
        
        
        
        
    
