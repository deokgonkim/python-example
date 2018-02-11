from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text = urlopen("https://www.dgkim.net/wordpress/").read()
soup = BeautifulSoup(text)

jobs = set()

for header in soup("div", "post"):
    #print "-" * 80
    #print header
    links = header('a')
    #print(" Links  : %s " % links)
    if not links: continue
    link = links[0]
    jobs.add("%s (%s)" % (link.string, link['href']))

print "=" * 80

print "\n".join(sorted(jobs, key=lambda s: s.lower()))
