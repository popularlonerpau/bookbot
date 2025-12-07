def num_of_words(text):
    dum = text.split()
    return dum

def num_of_characters(text):
    
    lowercs = text.lower()
    dictionar = {}
    for ch in lowercs:
        if ch in dictionar:
            dictionar[ch] += 1
        else:
            dictionar[ch] = 1    
    return dictionar


