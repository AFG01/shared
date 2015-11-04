import re

def count(string):
    
    """Remove symbols, digits, and punctuations except spaces from the
    the text and count total number of words and split the text"""
    punctuation = re.compile(r'[-.?!,"@:;()|0-9]')
    #pfs=punctuation/ number free text
    pfs = punctuation.sub("", string)
    word_list = str.split(pfs)
    count = len(word_list)
    return count, word_list