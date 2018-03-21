from nntplib import NNTP

#server = NNTP('news.easynews.com')
#server = NNTP('news.giganews.com')
#server = NNTP('news.mozilla.org')
server = NNTP('news.kornet.net')
print server.group('comp.lang.python.announce')[0]
print server.group('han.test')[0]
