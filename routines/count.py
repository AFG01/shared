def count(string):
    
    """Count the total number of letters in the text
    and convert the text into lowercase as well"""
    
    cap_txt = string.lower()
    #sft = Symbol/space/numbers Free text
    sft = ''.join(e for e in cap_txt if e.isalpha())
    count = len(sft)
    return count, sft