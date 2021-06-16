"""
@author: gpwolfe
"""
import csv
import spacy

nlp = spacy.load('/Users/piper/opt/anaconda3/envs/pyling/lib/python3.8/site-packages/en_core_web_md/en_core_web_md-2.3.1')
SPAM_WARN = 'This site uses Akismet to reduce spam.'

def process_text(fn, fn_out):
    """
    Remove duplicates, captions (short-length text) and spam notice.
    
    Generates a new csv file with duplicates, short texts and spam notice
    removed.

    Parameters
    ----------
    fn : string
        Input filename, csv file containing articles from scrapy.
    fn_out : string
        Output filename, csv file containing processed articles.

    Returns
    -------
    None.

    """
    with open(fn, 'r', newline='') as f:
        with open(fn_out, 'w', newline='') as out:
            reader = csv.reader(f)
            writer = csv.writer(out)
            texts = []
            texts2 = []
            for row in reader:
                to_write = row
                if SPAM_WARN in to_write[0]:
                    print('akismet')
                    start = to_write[0].index(SPAM_WARN)
                    end = start + len(SPAM_WARN)
                    to_write[0] = to_write[0][:start] + to_write[0][end:]
                if len(to_write[0]) > 20:
                    texts.append(to_write)

            for ix, article in enumerate(texts):
                unique = True
                checklen = len(article) - 5
                for ix2, article2 in enumerate(texts[ix+1:]):
                    if article[0][:checklen] == article2[0][:checklen]:
                        unique = False
                        print('duplicate', article[0][:20], article2[0][:20])
                if unique:
                    texts2.append(article)
            writer.writerows(texts2)


process_text('articles_10K.csv', 'articles_10K_out.csv')
process_text('articles_100K.csv', 'articles_100K_out.csv')

def spacy_csv(fn_in, fn_out):
    with open(fn_in, 'r') as f:
        with open(fn_out, 'a', newline='') as out:
            writer = csv.writer(out, delimiter=',')
            writer.writerow(['token', 'lemma', 'pos', 'tag', 'is_stop_word'])
            for line in f:
                doc1 = nlp(line)
                literals = [token.text for token in doc1]
                lemmas = [token.lemma_ for token in doc1]
                pos = [token.pos_ for token in doc1]
                tags = [token.tag_ for token in doc1]
                is_stop = [str(token.is_stop) for token in doc1]
                for token_data in zip(literals, lemmas, pos, tags, is_stop):
                    write_data = token_data
                    writer.writerow(write_data)

spacy_csv('articles_10K_out.csv', 'articles_10K_spacy.csv')
spacy_csv('articles_100K_out.csv', 'articles_100K_spacy.csv')
