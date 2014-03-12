import urllib

base = 'http://www.dspguide.com/CH%d.PDF'

N_chapters = 34

for n in range(N_chapters):
    url = base % (n + 1)
    fn = 'x/ch%02d.pdf' % (n+1)
    print 'Downloading %s in %s' % (url, fn)
    urllib.urlretrieve(url, fn)
