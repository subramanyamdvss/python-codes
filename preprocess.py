import numpy as np
import os, fnmatch
import csv
import operator
import pickle


def filter(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, "*questionID*"):
                continue
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def one_hot_preprocess():
    worddict={}
    files=filter('*question*','/home/surya/Downloads/vqa_data_share')
    for fl in files:
        with open(fl, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    if word=='':
                        continue
                    #word=filter(lambda ch: ch not in "?.!/;:,\ \n\t", word)
                    word = word.translate(None, ')?.!/;:,\ \n\t"')
                    if word.startswith("'"):
                        word=word[:-1]
                    if word.endswith("'"):
                        word=word[1:]
                    for wrd in  word.split('('):
                        if word in worddict:
                            worddict[word]+=1
                        else:
                            worddict[word]=1
            # reader = csv.reader(f, dialect='excel', delimiter=' ')
            # for row in reader:
            #     for word in row :
            #         if word=='':
            #             break;
            #         if word.endswith("\n") :
            #             word=word[0:-1]
            #         if word in worddict:
            #             worddict[word]+=1
            #         else:
            #             worddict[word]=1
    c=worddict.items()
    ls_tuples = sorted(worddict.items(), key=lambda tup: tup[1])
    word2ix={}
    for i in xrange(5746):
        word2ix[ls_tuples[i][0]]=i;
    pickle.dump( word2ix, open( "/home/surya/Documents/word2ix.p", "w" ) )

# def printdict():
#   with open( "/home/surya/Documents/word2ix.p", "rb" ) as fl:
#       word2ix = pickle.load( fl )
#       print word2ix["what"]


one_hot_preprocess()
