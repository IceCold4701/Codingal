#function to check whether
#first and last characters of word match
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("lists of words with first and last characters same\n",lst)
    return ctr
count=match_words(['abc','cfc','xyz','aba','1221'])
print("Number of words having first and last letter same",count)