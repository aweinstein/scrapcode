#!/usr/bin/env python

# Some tests using gensim
# http://nlp.fi.muni.cz/projekty/gensim/tut2.html

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
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
print corpus

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
doc_bow = [(0, 1), (1, 1)]
print doc_bow, '->', tfidf[doc_bow] # step 2 -- use the model to transform
                                    # vectors

# Apply a transformation to a whole corpus
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
     print doc

# Transformations can also be serialized, one on top of another, in a sort of
# chain:

lsi = models.LsiModel(corpus_tfidf,
                      id2word=dictionary,
                      num_topics=2) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original
                               # corpus: bow->tfidf->fold-in-lsi

print
lsi.print_topics(2)
