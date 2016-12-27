data='./europarl-v7.en'
new_word=["european","commission","president", "parliament", "council"]

f={}
for word in new_word:
    f[word]=open("corpus_"+word,'w')

ex_corpus=open("corpus_exclusive",'w')
    
cntn=open(data, 'r').readlines()

for L in cntn:
    L_lower=L.lower()
    
    new=False
    for word in new_word:
        if word in L_lower:
            f[word].write(L)
            new=True
    
    if not new: ex_corpus.write(L)
        