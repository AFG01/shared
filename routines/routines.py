import string
import numpy as np

def count(string):
    
    """Count the total number of letters in the text
    and convert the text into lowercase as well"""
    
    cap_txt = string.lower()
    #sft = Symbol/space/numbers Free text
    sft = ''.join(e for e in cap_txt if e.isalpha())
    count = len(sft)
    return count, sft

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
    """Creates a frequencies database"""
    frequencies = {'a': 11.602, 'b': 4.702, 'c': 3.511, 'd': 2.670, 'e': 2.007, 'f': 3.779, 'g': 1.950, 'h': 7.232, 'i': 6.286, 'j': 0.597, 'k': 0.590, 'l': 2.705, 'm': 4.383, 'n': 2.365, 'o': 6.264, 'p': 2.545, 'q': 0.173, 'r': 1.653, 's': 7.755, 't': 16.671, 'u': 1.487, 'v': 0.649, 'w': 6.753, 'x': 0.017, 'y': 1.620, 'z': 0.034}
    return frequencies

def guess(letter, text_input):
    """Makes a guess for the letter"""
    total, text = count(text_input)
    a = norm_freq(specific_freq(letter, text), total)
    
    w = create_data_base()['a']/100
    
    for c in string.ascii_lowercase:
        v = create_data_base()[c]/100
        if np.abs(v - a) <= np.abs(w - a):
            aux = c
            w = v
    return aux

def translation(text_input):
    new_alphabet = ''
    for h in string.ascii_lowercase:
        new_alphabet += guess(h, text_input)
    
    table = str.maketrans(string.ascii_lowercase, new_alphabet)
    text = text_input.lower().translate(table)
    return text
    
    
    
    
    
    
    
    