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
    print pp,nep,np,pne,nene,nne,pn,nen,nn
    accuracy = float(pp+nn+nene)/float(pp+pn+pne+np+nn+nne+nep+nen+nene)
    print accuracy
    precision_positive = float(pp)/float(pp+pne+pn)
    precision_negative = float(nn)/float(nn+np+nne)
    precision_neutral = float(nene)/float(nene+nep+nen)
    recall_positive = float(pp)/float(pp+nep+np)
    recall_negative = float(nn)/float(nn+pn+nen)
    recall_neutral = float(nene)/float(nene+pne+nne)

    if precision_positive+recall_positive != 0.:
        f_positive=(2*precision_positive*recall_positive)/(precision_positive+recall_positive)
    else:
        f_positive = "precision + recall positive = 0"

    if precision_negative+recall_negative != 0.:
        f_negative=(2*precision_negative*recall_negative)/(precision_negative+recall_negative)
    else:
        f_negative = "precision + recall negative = 0"

    if precision_neutral+recall_neutral != 0.:
        f_neutral=(2*precision_neutral*recall_neutral)/(precision_neutral+recall_neutral)
    else:
        f_neutral = "precision + recall neutral = 0"

    return accuracy,precision_positive,precision_negative,precision_neutral,recall_positive,recall_negative,recall_neutral,f_positive,f_negative,f_neutral
