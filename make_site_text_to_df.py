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
                                        'html.parser')
         self.text = ""
    
        
    def get_text(self):
        """
        Removes punctuation and extra spaces from the text and transforms all
        words to lowercase.
        
        Parameters
        ----------
        text : List
            A list of words from get_text. 


        Returns
        -------
        Updates self.text with a string of all text held within the <p> tags
        of the URL passed to the class instance.

        """
        all_ps = self.site_soup.find_all('p')
        all_ps_text = [x.get_text() for x in all_ps]
        texts_together = ' '.join(all_ps_text)
        text_no_punct_lower = re.sub(r'[^ \w]', '', texts_together).lower()
        text_one_space = re.sub(r' +', ' ', text_no_punct_lower)
        self.text = text_one_space.strip()
        
        
    
    def remove_text(self, beginning_cut, end_cut):
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
            front_split = self.text.split(beginning_cut)
        except: 
            InputError(f"\"{beginning_cut}\" doesn't seem to be here. Please check your beginning cut and type it exactly as it appears in the text.")
        try:
            back_split = front_split[1].split(end_cut)
        except:
            InputError(f"\"{end_cut}\" doesn't seem to appear after your beginning cut. Please check your end cut and type it exactly as it appears in the text.")
        # Check that beginning_cut and end_cut are unique          
        if len(front_split) > 2:
            raise InputError(f"\n\"{beginning_cut}\" occurs more than once in the text. \n Try typing more words for your beginning cut.")
        if len(back_split) > 2:
            raise InputError(f"\n\"{end_cut}\" occurs more than once after your beginning cut. \n Try typing more words for your end cut.")
        new_text = front_split[0] + back_split[1]
        cut_okay = input(f"\"{new_text.strip()}\"  <<< Does this look right? Y/N: ")
        if cut_okay == 'Y' or cut_okay == 'y':
            print("Okay, text removed!")
            self.text = re.sub(r' +', ' ', new_text).strip()
        elif cut_okay == 'N' or cut_okay == 'n':
            print("No text removed. Please try again.")
        else:
            print("Sorry, didn't understand that. Please try again.")
'''
Next step: make the try/except into if-else, or else figure out how to break after
the exception
''' 
            
            
        

        
        
        
        
        
        
        
    
