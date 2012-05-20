import logging
import sys

from gensim.corpora import WikiCorpus
from gensim.corpora.mmcorpus import MmCorpus

if __name__ == '__main__':

    # Log both to a file and the console
    log_name = 'tut4.log'
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_name)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info("running %s" % ' '.join(sys.argv))

    fname = 'simplewiki-20120313-pages-articles.xml.bz2'
    wiki = WikiCorpus(fname)
    # save dictionary and bag-of-words (term-document frequency matrix)

    output = 'simple_wiki'
    wiki.dictionary.save_as_text(output + '_wordids.txt')
    MmCorpus.serialize(output + '_bow.mm', wiki, progress_cnt=10000)
    del wiki
