import itertools
import sys
import os.path
import re
import bz2

from gensim import utils

DEFAULT_DICT_SIZE = 50000
ARTICLE_MIN_CHARS = 500

RE_P0 = re.compile('<!--.*?-->', re.DOTALL | re.UNICODE) # comments
RE_P1 = re.compile('<ref([> ].*?)(</ref>|/>)', re.DOTALL | re.UNICODE) # footnotes
RE_P2 = re.compile("(\n\[\[[a-z][a-z][\w-]*:[^:\]]+\]\])+$", re.UNICODE) # links to languages
RE_P3 = re.compile("{{([^}{]*)}}", re.DOTALL | re.UNICODE) # template
RE_P4 = re.compile("{{([^}]*)}}", re.DOTALL | re.UNICODE) # template
RE_P5 = re.compile('\[(\w+):\/\/(.*?)(( (.*?))|())\]', re.UNICODE) # remove URL, keep description
RE_P6 = re.compile("\[([^][]*)\|([^][]*)\]", re.DOTALL | re.UNICODE) # simplify links, keep description
RE_P7 = re.compile('\n\[\[[iI]mage(.*?)(\|.*?)*\|(.*?)\]\]', re.UNICODE) # keep description of images
RE_P8 = re.compile('\n\[\[[fF]ile(.*?)(\|.*?)*\|(.*?)\]\]', re.UNICODE) # keep description of files
RE_P9 = re.compile('<nowiki([> ].*?)(</nowiki>|/>)', re.DOTALL | re.UNICODE) # outside links
RE_P10 = re.compile('<math([> ].*?)(</math>|/>)', re.DOTALL | re.UNICODE) # math content
RE_P11 = re.compile('<(.*?)>', re.DOTALL | re.UNICODE) # all other tags
RE_P12 = re.compile('\n(({\|)|(\|-)|(\|}))(.*?)(?=\n)', re.UNICODE) # table formatting
RE_P13 = re.compile('\n(\||\!)(.*?\|)*([^|]*?)', re.UNICODE) # table cell formatting
RE_P14 = re.compile('\[\[Category:[^][]*\]\]', re.UNICODE) # categories

# Replace RE_P7 and RE_P8
# It doesn't work: I get a runaway for some inputs
## RE_P15 = re.compile('\[\[[fF]ile:.*(\|.*)*\|(.*)\]\]', re.UNICODE) # File
## RE_P16 = re.compile('\[\[[iI]mage:.*(\|.*)*\|(.*)\]\]', re.UNICODE) # Image

RE_P15 = re.compile('\[\[([fF]ile:|[iI]mage)[^]]*(\]\])', re.UNICODE)

def filter_wiki(raw):
    """
    Filter out wiki mark-up from `raw`, leaving only text. `raw` is either unicode
    or utf-8 encoded string.
    """
    # parsing of the wiki markup is not perfect, but sufficient for our purposes
    # contributions to improving this code are welcome :)
    text = utils.decode_htmlentities(utils.to_unicode(raw, 'utf8', errors='ignore'))
    text = utils.decode_htmlentities(text) # '&amp;nbsp;' --> '\xa0'
    return remove_markup(text)

def remove_markup(text):
    text = re.sub(RE_P2, "", text) # remove the last list (=languages)
    # the wiki markup is recursive (markup inside markup etc)
    # instead of writing a recursive grammar, here we deal with that by removing
    # markup in a loop, starting with inner-most expressions and working outwards,
    # for as long as something changes.
    text = remove_template(text)
    text = remove_file(text)
    iters = 0
    while True:
        old, iters = text, iters + 1
        text = re.sub(RE_P0, "", text) # remove comments
        text = re.sub(RE_P1, '', text) # remove footnotes
        text = re.sub(RE_P9, "", text) # remove outside links
        text = re.sub(RE_P10, "", text) # remove math content
        text = re.sub(RE_P11, "", text) # remove all remaining tags
        text = re.sub(RE_P14, '', text) # remove categories
        text = re.sub(RE_P5, '\\3', text) # remove urls, keep description
        text = re.sub(RE_P6, '\\2', text) # simplify links, keep description only
        # remove table markup
        text = text.replace('||', '\n|') # each table cell on a separate line
        text = re.sub(RE_P12, '\n', text) # remove formatting lines
        text = re.sub(RE_P13, '\n\\3', text) # leave only cell content
        # remove empty mark-up
        text = text.replace('[]', '')
        if old == text or iters > 2: # stop if nothing changed between two iterations or after a fixed number of iterations
            break

    # the following is needed to make the tokenizer see '[[socialist]]s' as a single word 'socialists'
    # TODO is this really desirable?
    text = text.replace('[', '').replace(']', '') # promote all remaining markup to plain text
    return text

def remove_markup_original(text):
    text = re.sub(RE_P2, "", text) # remove the last list (=languages)
    # the wiki markup is recursive (markup inside markup etc)
    # instead of writing a recursive grammar, here we deal with that by removing
    # markup in a loop, starting with inner-most expressions and working outwards,
    # for as long as something changes.
    iters = 0
    while True:
        old, iters = text, iters + 1
        text = re.sub(RE_P0, "", text) # remove comments
        text = re.sub(RE_P1, '', text) # remove footnotes
        text = re.sub(RE_P9, "", text) # remove outside links
        text = re.sub(RE_P10, "", text) # remove math content
        text = re.sub(RE_P11, "", text) # remove all remaining tags
        # remove templates (no recursion)
        text = re.sub(RE_P3, '', text)
        text = re.sub(RE_P4, '', text)
        text = re.sub(RE_P14, '', text) # remove categories
        text = re.sub(RE_P5, '\\3', text) # remove urls, keep description
        text = re.sub(RE_P7, '\n\\3', text) # simplify images, keep description only
        text = re.sub(RE_P8, '\n\\3', text) # simplify files, keep description only
        text = re.sub(RE_P6, '\\2', text) # simplify links, keep description only
        # remove table markup
        text = text.replace('||', '\n|') # each table cell on a separate line
        text = re.sub(RE_P12, '\n', text) # remove formatting lines
        text = re.sub(RE_P13, '\n\\3', text) # leave only cell content
        # remove empty mark-up
        text = text.replace('[]', '')
        if old == text or iters > 2: # stop if nothing changed between two iterations or after a fixed number of iterations
            break

    # the following is needed to make the tokenizer see '[[socialist]]s' as a single word 'socialists'
    # TODO is this really desirable?
    text = text.replace('[', '').replace(']', '') # promote all remaining markup to plain text
    return text


def tokenize(content):
    """
    Tokenize a piece of text from wikipedia. The input string `content` is assumed
    to be mark-up free (see `filter_wiki()`).

    Return list of tokens as utf8 bytestrings. Ignore words shorted than 2 or longer
    that 15 characters (not bytes!).
    """
    # TODO maybe ignore tokens with non-latin characters? (no chinese, arabic, russian etc.)
    return [token.encode('utf8') for token in utils.tokenize(content, lower=True, errors='ignore')
            if 2 <= len(token) <= 15 and not token.startswith('_')]



def get_texts(fname, return_raw=False):
    """
    Iterate over the dump, returning text version of each article.

    Only articles of sufficient length are returned (short articles & redirects
    etc are ignored).

    Note that this iterates over the **texts**; if you want vectors, just use
    the standard corpus interface instead of this function::

    >>> for vec in wiki_corpus:
    >>>     print vec
    """
    articles, articles_all = 0, 0
    intext, positions = False, 0
    for lineno, line in enumerate(bz2.BZ2File(fname)):
        if line.startswith('      <text'):
            intext = True
            line = line[line.find('>') + 1 : ]
            lines = [line]
        elif intext:
            lines.append(line)
        pos = line.find('</text>') # can be on the same line as <text>
        if pos >= 0:
            articles_all += 1
            intext = False
            if not lines:
                continue
            lines[-1] = line[:pos]
            # for debug
            raw_text = ''.join(lines)
            #print raw_text
            text = filter_wiki(''.join(lines))
            if len(text) > ARTICLE_MIN_CHARS: # article redirects are pruned here
                articles += 1
                if return_raw:
                    result = text
                    yield result
                else:
                    result = tokenize(text) # text into tokens here
                    positions += len(result)
                    yield raw_text,result

def get_raw_line(fname):
    for line in bz2.BZ2File(fname):
        yield line

def remove_file(s):
    for match in re.finditer(RE_P15, s):
        m = match.group(0)
        caption = m[:-2].split('|')[-1]
        s = s.replace(m, caption, 1)
    return s

def remove_template(s):
    n_open, n_close = 0, 0
    starts, ends = [], []
    in_template = False
    prev_c = None
    for i, c in enumerate(iter(s)):
        if not in_template:
            if c == '{' and c == prev_c:
                starts.append(i-1)
                in_template = True
                n_open = 1
        if in_template:
            if c == '{':
                n_open += 1
            elif  c == '}':
                n_close += 1
            if n_open == n_close:
                ends.append(i)
                in_template = False
                n_open, n_close = 0, 0
        prev_c = c

    s = ''.join([s[end+1:start] for start,end in 
                 zip(starts + [None], [-1] + ends )])

    return s

def text_filtering(articles):
    sep = 79 * '#'
    s_problems = []
    from time import time
    print sep
    start = time()
    for i,article in enumerate(articles):

        raw, txt = article
        elapsed = time() - start

        if i % 100 == 0:
            print i

        if elapsed > 0.5:
            s_problems.append(raw)
            print i
            if len(raw) > l:
                print raw[:l]
            else:
                print raw
        start = time()

fname = 'simplewiki-20120313-pages-articles.xml.bz2'

articles = get_texts(fname)
## articles_raw = get_texts(fname, True)
## lines = get_raw_line(fname)
        
s1 = """{{CalendarCustom|year={{{year|{{#time:Y}}}}}|month=04|float=right}}
'''April''' is the fourth [[month]] of the [[year]]. It has 30 [[day]]s. 
The name April comes from that [[Latin]] word ''aperire'' which means 
&quot;to open&quot;. This probably refers to growing [[plant]]s in 
spring. April begins on the same day of week as [[July]] in all years
and also [[January]] in leap years. 
April's [[flower]] is the [[Sweet Pea]]. Its [[birthstone]] is the 
[[diamond]]. The meaning of the diamond is innocence. 

== April in poetry == 
[[poetry|Poets]] use ''April'' to mean the end of winter. For example: 
''April showers bring [[May]] flowers.'' 

== Events in April ==
* [[April Fools' Day]] occurs on [[April 1]].
* [[Easter]] occurs on a [[week|Sunday]] between [[March 22]] and 
[[April 25]].
* [[Australia]] and [[New Zealand]] celebrate [[ANZAC Day]] on 25 April. 
[http://www.awm.gov.au/dawn/spirit/meaning.asp ANZAC] means Australian 
and New Zealand Army Corps, and began in 1915.

Hello {something} else.

And this is a lonely curly bracket { just to see what happens.
{{Months}}

{{Stub}}
 
[[af:April]]
[[als:April]]"""

s2 = """[[File:Chemin montant dans les hautes herbes.png|thumb|300px|This painting by [[Renoir]] is a work of art.]]

The word '''art''' is used to describe some activities or creations of [[human beings]] that have importance to the human [[mind]], regarding an attraction to the human [[senses]]. Therefore, art is made when a human expresses himself or herself. Some art is useful in a practical sense, such as a sculptured clay [[bowl]] that one can put things in. Many people disagree on how to define art. Many people say people are driven to make art due to their inner [[creativity]]. Art includes [[drawing]], [[painting]], [[sculpting]], [[photography]], [[Performing arts|performance art]], [[dance]], [[music]], [[poetry]], [[prose]] and [[theatre]].
"""
s3 = open('wiki1.txt').read()
