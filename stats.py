def num_of_words(text):
    dum = text.split()
    return len(dum)

def num_of_characters(text):
    
    lowercs = text.lower()
    dictionar = {}
    for ch in lowercs:
        if ch in dictionar:
            dictionar[ch] += 1
        else:
            dictionar[ch] = 1    
    return dictionar


def helper_function(helpy):
    return helpy["num"]

def sorted_list(g):
    new_dict = []
    for k, v in g.items():
        lil_dict = {}
        lil_dict["char"] = k
        lil_dict["num"]= v  
        new_dict.append(lil_dict)
    new_dict.sort(reverse= True, key=helper_function)
    return new_dict