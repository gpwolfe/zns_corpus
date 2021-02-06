#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:05:00 2020

@author: piper
"""

from bs4 import BeautifulSoup
import re
import requests

class InputError(Exception):
    pass
    
class SiteText:
    """
    Pass site URL as a string
    """
    
    def __init__(self, site):
         self.site = site
         self.site_html = requests.get(self.site)
         self.site_soup = BeautifulSoup(self.site_html.content, 'html.parser')
         self.text = "No processed text yet. Run SiteText.get_text()"
         self.raw_text = "No raw text yet. Run SiteText.get_raw_text()"
    
    def get_raw_text(self, remove_privacy_notice = True):
        """
        Gathers the text from <p> tags in site_html.

        Parameters
        ----------
        

        Returns
        -------
        None.

        """
        # Removing the privacy notice corresp. to last <p> element
        if remove_privacy_notice:
            privacy_notice = re.compile("akismet\w*")
            rem_element = self.site_soup.find_all(attrs={"class":privacy_notice})
            removed = []
            if len(rem_element) > 0:     
                for i in rem_element:
                    removed = i.extract()
        all_ps = self.site_soup.find_all('p')
        all_ps = [x.get_text() for x in all_ps]
        texts_together = ' '.join(all_ps)
        self.raw_text = texts_together

    def get_text(self, remove_privacy_notice = True):
        """
        Removes punctuation and extra spaces from the text and transforms all
        words to lowercase.
        
        Parameters
        ----------
        remove_privacy_notice : boolean, optional
            Removes the common privacy notice on ZNS website news pages. Set
            to False if you want to keep the privacy notice in the processed 
            text.
            The default is True.


        Returns
        -------
        Updates self.text with a string of all text held within the <p> tags
        of the URL passed to the class instance, minus the privacy notice if
        remove_privacy_notice is set to True (default).
        
        """
        if remove_privacy_notice:
            privacy_notice = re.compile("akismet\w*")
            rem_element = self.site_soup.find_all(attrs={"class":privacy_notice})
            removed = []
            if len(rem_element) > 0:     
                for i in rem_element:
                    removed = i.extract()   
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
        if beginning_cut in self.text:
            front_split = self.text.split(beginning_cut)
            if len(front_split) > 2:
                raise InputError(f"\n\"{beginning_cut}\" occurs more than once in the text. \n Try typing more words for your beginning cut.")
        else:
            raise InputError(f"\"{beginning_cut}\" is not in the text. Please check your beginning cut and type it exactly as it appears in the text.")
        if end_cut in front_split[1]:
            back_split = front_split[1].split(end_cut)
            if len(back_split) > 2:
                raise InputError(f"\n\"{end_cut}\" occurs more than once after your beginning cut. \n Try typing more words for your end cut.")
        else:
            raise InputError(f"\"{end_cut}\" doesn't appear after your beginning cut. Please check your end cut and type it exactly as it appears in the text.")
        new_text = front_split[0] + back_split[1]
        cut_okay = input(f"\"{new_text.strip()}\"\n^^^ Does this look right? Y/N: ")
        if cut_okay == 'Y' or cut_okay == 'y':
            print("Okay, text removed!")
            self.text = re.sub(r' +', ' ', new_text).strip()
        elif cut_okay == 'N' or cut_okay == 'n':
            print("No text removed. Please try again.")
        else:
            print("Sorry, didn't understand that. Please try again.")
    