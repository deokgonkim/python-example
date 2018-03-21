from nntplib import NNTP

#server = NNTP('news.easynews.com')
#server = NNTP('news.giganews.com')
#server = NNTP('news.mozilla.org')
server = NNTP('news.kornet.net')
print server.group('comp.lang.python.announce')[0]
"""
 |  group(self, name)
 |      Process a GROUP command.  Argument:
 |      - group: the group name
 |      Returns:
 |      - resp: server response if successful
 |      - count: number of articles (string)
 |      - first: first article number (string)
 |      - last: last article number (string)
 |      - name: the group name
"""
group = server.group('han.test')
print repr(group)

first = group[2]
last = group[3]

print "first ", first
print "last ", last

i = 0
for id in range(int(first), int(last)):
    i += 1
    print(server.article(str(id)))
    if i == 10: break;

server.quit()
