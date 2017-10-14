"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
Functions to evaluate the performance of our model
"""


def evaluation(real_sentiments,compute_sentiments):
    pp=0
    nep=0
    np=0
    pne=0
    nene=0
    nne=0
    pn=0
    nen=0
    nn=0
    for i in range(0,len(real_sentiments)):
        if real_sentiments[i]==compute_sentiments[i]:
            if(real_sentiments[i]=="positive"):
                pp+=1
            elif (real_sentiments[i]=="negative"):
                nn+=1
            else :
                nene+=1
        else:
            if compute_sentiments[i]=="positive" and real_sentiments[i]=="neutral":
                pne+=1
            elif compute_sentiments[i]=="positive" and real_sentiments[i]=="negative":
                pn+=1
            elif compute_sentiments[i]=="neutral" and real_sentiments[i]=="positive":
                nep+=1
            elif compute_sentiments[i]=="neutral" and real_sentiments[i]=="negative":
                nen+=1
            elif compute_sentiments[i]=="negative" and real_sentiments[i]=="positive":
                np+=1
            elif compute_sentiments[i]=="negative" and real_sentiments[i]=="neutral":
                nne+=1
    accuracy=(pp+nn+nene)/(pp+pn+pne+np+nn+nne+nep+nen+nene)
    precision_positive=pp/(pp+pne+pn)
    precision_negative=nn/(nn+np+nne)
    precision_neutral=nene/(nene+nep+nen)
    recall_positive=pp/(pp+nep+np)
    recall_negative=nn/(nn+pn+nen)
    recall_neutral=nene/(nene+pne+nne)
    f_positive=(2*precision_positive*recall_positive)/(precision_positive+recall_positive)
    f_negative=(2*precision_negative*recall_negative)/(precision_negative+recall_negative)
    f_neutral=(2*precision_neutral*recall_neutral)/(precision_neutral+recall_neutral)
    return accuracy,precision_positive,precision_negative,precision_neutral,recall_positive,recall_negative,recall_neutral,f_positive,f_negative,f_neutral