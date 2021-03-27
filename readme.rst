This project is intended as a practice exercise in web scraping and natural
language processing, with the end goal of creating a useful corpus from
the content of the website of ZNS Bahamas. 

make_site_text_to_df.py is being used to create a friendly, consistent web scraping 
object, usable by those with minimal Python experience. The site_text object 
returns a BeautifulSoup object containing site elements with <p> tags, which 
hold the relevant text on the ZNS Bahamas website. site_text has a method for 
extracting the text from the <p> objects, and a method for modifying the resulting 
text by removing extraneous site text, such as notices that may appear on many pages,
and which may be undesirable to include in a corpus, as creating statistical outliers.


