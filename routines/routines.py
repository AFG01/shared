import string
import numpy as np
import re

def count(string):
    
    """Count the total number of letters in the text
    and convert the text into lowercase as well"""
    
    cap_txt = string.lower()
    #sft = Symbol/space/numbers Free text
    sft = ''.join(e for e in cap_txt if e.isalpha())
    count = len(sft)
    return count, sft

def word_count(string):
    
    """Remove symbols, digits, and punctuations except spaces from the
    the text and count total number of words and split the text"""
    punctuation = re.compile(r'[-.?!,"@:;()|0-9]')
    #pfs=punctuation/ number free text
    pfs = punctuation.sub("", string.lower())
    word_list = str.split(pfs)
    count = len(word_list)
    return count, word_list

def freq_word_letter(letter, word_list, count):
    occur = 0
    for i in word_list:
        if i[0] == letter:
            occur += 1
    frequency = occur/count
    return frequency
 

def norm_freq(specific, total):
    """Calculates normalised frequency"""
    return specific/total


def specific_freq(letter, text):
    """Calculates frequency of a specific letter in a text"""
    ocur = 0
    for c in text:
        if c == letter:
            ocur += 1
    return ocur

def create_data_base():
    """Creates a frequencies database from Wiki. In %"""
    frequencies = {'a': 11.602, 'b': 4.702, 'c': 3.511, 'd': 2.670, 'e': 2.007, 'f': 3.779, 'g': 1.950, 'h': 7.232, 'i': 6.286, 'j': 0.597, 'k': 0.590, 'l': 2.705, 'm': 4.383, 'n': 2.365, 'o': 6.264, 'p': 2.545, 'q': 0.173, 'r': 1.653, 's': 7.755, 't': 16.671, 'u': 1.487, 'v': 0.649, 'w': 6.753, 'x': 0.017, 'y': 1.620, 'z': 0.034}
    return frequencies

def create_data_base_c():
    """Creates a frequencies database from Cornell Math. In %"""
    frequencies = {'a': 8.12, 'b': 1.49, 'c': 2.71, 'd': 4.32, 'e': 12.02, 'f': 2.30, 'g': 2.03, 'h': 5.92, 'i': 7.31, 'j': 0.10, 'k': 0.69, 'l': 3.98, 'm': 2.61, 'n': 6.95, 'o': 7.68, 'p': 1.82, 'q': 0.11, 'r': 6.02, 's': 6.28, 't': 9.10, 'u': 2.88, 'v': 1.11, 'w': 2.09, 'x': 0.17, 'y': 2.11, 'z': 0.07}
    return frequencies

def create_data_base_1():
    """Creates a frequencies database for first letter of a word from Wiki. In %"""
    frequencies = {'a': 11.602, 'b': 4.702, 'c': 3.511, 'd': 2.670, 'e': 2.007, 'f': 3.779, 'g': 1.950, 'h': 7.232, 'i': 6.286, 'j': 0.597, 'k': 0.590, 'l': 2.705, 'm': 4.383, 'n': 2.365, 'o': 6.264, 'p': 2.545, 'q': 0.173, 'r': 1.653, 's': 7.755, 't': 16.671, 'u': 1.487, 'v': 0.649, 'w': 6.753, 'x': 0.017, 'y': 1.620, 'z': 0.034}
    return frequencies
    
def guess(letter, text_input):
    """Makes a guess for the letter"""
    total, text = count(text_input)
    a = norm_freq(specific_freq(letter, text), total)
    
    w = (create_data_base()['a'] + create_data_base_c()['a'])/200
    
    for c in string.ascii_lowercase:
        v = (create_data_base()[c] + create_data_base_c()[c])/200
        if np.abs(v - a) <= np.abs(w - a):
            aux = c
            w = v
    return aux

def guess_1(letter, count, word_list):
    """Makes a guess for first letter in each word"""
    a = freq_word_letter(letter, word_list, count)
    
    w = create_data_base_1()['a']/100
    
    for c in string.ascii_lowercase:
        v = create_data_base_1()[c]/100
        if np.abs(v - a) <= np.abs(w - a):
            aux = c
            w = v
    return aux
    
def translation_raw(text_input):
    """Makes a translation table and translates the text. Word by word, each first letter is guessed indepently with relative first letter frequency. The other letters in the world are guessed via independent frequency in the whole text"""
    
    count, word_list = word_count(text_input)
    
    new_1_alphabet = ''
    for h in string.ascii_lowercase:
        new_1_alphabet += guess_1(h, count, word_list)
        
    table_1 = str.maketrans(string.ascii_lowercase, new_1_alphabet)
    
    
    new_alphabet = ''
    for h in string.ascii_lowercase:
        new_alphabet += guess(h, text_input)
    
    table = str.maketrans(string.ascii_lowercase, new_alphabet)
    
    new_list = []
    for word in word_list:
        inw = word[0].translate(table_1)
        endw = word[1:].translate(table)
        new_list.append(inw+endw)
    
    return ' '.join(new_list)
      

def frequency_each_letter(text):
    new_freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
               'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
               'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 
               'x': 0, 'y': 0, 'z': 0}
    for c in text:
        for h in string.ascii_lowercase:
            if c == h:
                new_freq[c] +=1
    return new_freq

def translation_step(text_input, number):
    
    create_data_base_c()
    frequency_each_letter(text_input.lower())
    data_freq_ordered
    text_freq_ordered
    
    alphabet = ''
    new_alphabet = ''
    for n in range(0, number):
        alphabet = alphabet.join(data_freq_ordered[n])
        new_alphabet = new_alphabet.join(text_freq_ordered[n])
    
    table = str.maketrans(alphabet, new_alphabet.upper())
    
    text = text_input.translate(table)
                
    return text
    
    
    
    
    
    