#!/usr/bin/env python

# Some tests using gensim
# http://nlp.fi.muni.cz/projekty/gensim/tut1.html

# So we don't run the installed version, but the github one.
import sys
try:
    sys.path.remove('/usr/local/lib/python2.6/dist-packages/gensim-0.7.8-py2.6.egg')
except ValueError:
    pass
gensim_path = '/home/ajw/projects/pycode/gensim/'
if sys.path.count(gensim_path) == 0:
    sys.path.insert(0, gensim_path)

import logging
from gensim import corpora


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

print texts
# remove words that appear only once
allTokens = sum(texts, [])
tokensOnce = set(word for word in set(allTokens) if allTokens.count(word) == 1)
texts = [[word for word in text if word not in tokensOnce]
         for text in texts]

print texts

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference
print dictionary
print dictionary.token2id # Mapping between words and their Ids

newDoc = "Human computer interaction"
newVec = dictionary.doc2bow(newDoc.lower().split())
print newVec # the word "interaction" does not appear in the dictionary and is
             # ignored

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for
                                                         # later use
print corpus


# If the corpus is big, we don't want to have it in memory.  Gensim only
# requires that a corpus must be able to return one document vector at a time:
class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus()

# Similarly, to construct the dictionary without loading all texts into memory:

# collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for
                                line in open('mycorpus.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems()
            if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that
                                              # appear only once
dictionary.compactify() # remove gaps in id sequence after words that were
                        # removed
print dictionary
