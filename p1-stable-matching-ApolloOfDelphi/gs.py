# Tyler Moore
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CYB 2013

def gs(men, women, pref):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank={}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m]=i
            i+=1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)    #initially all men and women are free
    numpartners = len(men) 
    S = {}           #build dictionary to store engagements 

    #run the algorithm
    while freemen:
        m = freemen.pop()
        #get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m]+=1
        if w not in S: S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

def gs_block(men, women, pref, blocked):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    "need to make an if statement for blockedPair in blocked"
     # preprocessing
    ## build the rank dictionary
    rank={}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m]=i
            i+=1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)    #initially all men and women are free
    numpartners = len(men) 
    S = {}           #build dictionary to store engagements 

    #run the algorithm
    #blockedwoman = "base"
    while freemen:
        m = freemen.pop()
        #find blocked woman for the man
        ##for blockedset in blocked:
            ##if blockedset[0] == m:
                ##blockedwoman=blockedset[1]
        #get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m]+=1
        if prefptr[m] >= numpartners: break
        if tuple((m,w)) in blocked:
            freemen.add(m)
        if w not in S: S[w] = m #if woman has match then no 
        else: #else then check for match
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

def gs_tie(men, women, preftie):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of sets of preferred names in sorted order)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    matches={}
    freemen = set(men)
    while freemen:
        proposeE = freemen.pop()
        manpref = preftie[proposeE]
        for group in manpref:
            for induvidual in group:
                if proposeE in matches.values(): 
                    break
                if induvidual not in matches:
                    matches[induvidual] = proposeE
                    break #Doesnt Break origional for loop

                else:
                    old_guy = matches[induvidual]
                    woman_pref = preftie[induvidual]
                    for men in woman_pref:
                        if old_guy in men:
                            old_guy_position = woman_pref.index(men)
                        if proposeE in men:
                            proposeE_position = woman_pref.index(men)
                           
                           
                    if proposeE_position < old_guy_position:
                        matches[induvidual] = proposeE
                        freemen.add(old_guy)
                    else:
                        freemen.add(proposeE)


    return matches

if __name__=="__main__":
    #input data
    themen = ['xavier','yancey','zeus']
    thewomen = ['amy','bertha','clare']

    thepref = {'xavier': ['amy','bertha','clare'],
           'yancey': ['bertha','amy','clare'],
           'zeus': ['amy','bertha','clare'],
           'amy': ['yancey','xavier','zeus'],
           'bertha': ['xavier','yancey','zeus'],
           'clare': ['xavier','yancey','zeus']
           }
    thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}],
           'yancey': [{'amy','bertha'},{'clare'}],
           'zeus': [{'amy'},{'bertha','clare'}],
           'amy': [{'zeus','xavier','yancey'}],
           'bertha': [{'zeus'},{'xavier'},{'yancey'},],
           'clare': [{'xavier','yancey'},{'zeus'}]
           }
    
    blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}

    #eng

    ##match = gs(themen,thewomen,thepref)
    ##print(match)
    
    ##match_block = gs_block(themen,thewomen,thepref,blocked)
    ##print(match_block)

    match_tie = gs_tie(themen,thewomen,thepreftie)
    print(match_tie)
    