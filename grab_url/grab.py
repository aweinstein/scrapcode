#!/usr/bin/env python

import urllib2

## f = urllib2.urlopen('http://personalpages.tds.net/~kent37/kk/00010.html')
## data = f.read()
## f.close()

## print data[:200]


# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('CsmSoup', '138.67.19.2', 'cool', 'csm')
opener = urllib2.build_opener(auth_handler)

url = '''http://138.67.19.2/archive/fetch?swid=/CSMBERTHOUDHALL9A/LONTRUNK/VAVS/BOXCONTROLLOGIC/LOWSPACETEMPLOG&content-type=text/comma-separated-values&after=2011-04-18T00:00&before=2011-04-28T23:59'''
#print url
url_template = '''http://138.67.19.2/archive/fetch?swid=%s&content-type=text/comma-separated-values&after=2011-04-18T00:00&before=2011-04-28T23:59'''

name = '/CSMSOUP/CSMCTLM/CTLM2/AHU3/LOGS/RAH'
name = '/CSMSOUP/CSMCTLM/CTLM2/VAVS/FIRSTLEVEL/VAV_SA142/LOGS/AIRFLOW'

url = url_template % name
#print url 
data = opener.open(url).read()

print data
