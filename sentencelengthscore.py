final = []
def sentencelen():
    sentence="I am a boy. your name is saad. can you explain it to me"
    sentlen=len(sentence)
    #print(sentlen)
    sentence=sentence.split('.')
    #print(sentence)
    for i in sentence:
        ilen=len(i)
        alpha=ilen**0.5
        alpha=1/alpha
        results=alpha
        results=final.append(results)
        final.sort()
        maximum=max(final)
    for x in final:
        print(x/maximum)
        #print(x/maximum)
sentencelen()
