#!/usr/bin/env python

# Some tests using gensim
# http://nlp.fi.muni.cz/projekty/gensim/tut3.html

import logging
from pprint import pprint

from gensim import corpora, models, similarities

logging.root.setLevel(logging.INFO) # will suppress DEBUG level events


dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
print corpus

lsi = models.LsiModel(corpus, id2word=dictionary, numTopics=2)

doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
print vec_lsi
index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI
                                                   # space and index it
index.save('/tmp/deerwester.index')
index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')

sims = index[vec_lsi] # perform a similarity query against the corpus
print list(enumerate(sims))

sims = sorted(enumerate(sims), key=lambda item: -item[1])
pprint(sims)
