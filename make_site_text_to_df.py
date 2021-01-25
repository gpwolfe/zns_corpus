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

class site_text:
    """
    Pass site URL as a string
    """
    
    def __init__(self, site):
         self.site = site
         
         self.site_html = requests.get(self.site)
         self.site_soup = BeautifulSoup(self.site_html.content, 
                                        'html.parser').prettify()
         
         
    def soupify(self):
        self.site_html = requests.get(self.site)
        self.site_soup = BeautifulSoup(self.site_html.content, 'html.parser')
        self.site_soup.prettify()
        return self.site_soup
    
    def process(self):
        """
        Removes punctuation and extra spaces from the text and transforms all
        words to lowercase.

        Returns
        -------
        None.

        """
    
    def remove_text(self, beginning_text, end_text):
        """
        Uses regular expressions to match beginning_text and end_text. Deletes
        all text, starting with the first character of beginning_text, ending 
        with last character of end_text

        Parameters
        ----------
        beginning_text : string
            A unique string in the site text that is included in the text to
            be deleted.
        end_text : string
            A string that appears after the beginning_text. Will be included
            in the deletion.

        Returns
        -------
        None.

        """
        
        
        
        
        
        
        
        
        
        
    
