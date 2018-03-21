from nntplib import NNTP
from time import strftime, time, localtime
from email import message_from_string
from urllib import urlopen
import textwrap
import re

day = 24 * 60 * 60

def wrap(string, max=70):
    """
    Wraps a string to a maximum line width.
    """

    return '\n'.join(textwrap.wrap(string)) + '\n'

class NewsAgent:
    """
    An object that can distribute news items from news
    sources to news destinations
    """
    def __init__(self):
        self.sources = []
        self.destinations = []

    def addSource(self, source):
        self.sources.append(source)

    def addDestination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        """
        Retrieve all news items from all sources, and
        Distribute them to all destinations.
        """
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.recieveItems(items)

class NewsItem:
    """
    A simple news item consisting of a title and body text.
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body

class NNTPSource:
    """
    A news source that retrieves news items from an NNTP group.
    """
    def __init__(self, servername, group, window):
        self.servername = servername
        self.group = group
        self.window = window

    def getItems(self):
        server = NNTP(self.servername)
        group = server.group(self.group)
        first = group[2]
        last = str(int(group[2]) + 10)
        #last = str(int(group[2]) + 2)

        for id in range(int(first), int(last)):
            lines = server.article(str(id))[3]
            message = message_from_string('\n'.join(lines))

            title = message['subject']
            #print(repr(dir(message)))
            print(message.get_content_type())
            if 'text' in message.get_content_type():
                body = message.get_payload()
            else:
                body = 'Body is not text'
            if 'ybegin' in message.get_payload():
                body = 'hmm'

            if message.is_multipart():
                #body = body[0]
                body = 'Multi part is not implemented yet'

            yield NewsItem(title, body)

        server.quit()

    def getItems_(self):
        start = localtime(time() - self.window * day)
        date = strftime('%y%m%d', start)
        hour = strftime('%H%M%S', start)

        server = NNTP(self.servername)


        ids = server.newnews(self.group, date, hour)[1]

        for id in ids:
            lines = server.article(id)[3]
            message = message_from_string('\n'.join(lines))

            title = message['subject']
            body = message.get_payload()

            if message.is_multipart():
                body = body[0]

            yield NewsItem(title, body)

        server.quit()

class SimpleWebSource:
    """
    A news sources that extracts news items from a web page using
    regular expressions.
    """

    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        titles = self.titlePattern.findall(text)
        bodies = self.bodyPattern.findall(text)
        for title, body in zip(titles, bodies):
            yield NewsItem(title, wrap(body))

class PlainDestination:
    """
    A news destination that formats all its news items as plain text.
    """
    def recieveItems(self, items):
        for item in items:
            print item.title
            print '-'*len(item.title)
            print item.body

class HTMLDestination:
    """
    A news destination that formats all its news items as HTML.
    """

    def __init__(self, filename):
        self.filename = filename

    def recieveItems(self, items):
        out = open(self.filename, 'w')
        print >> out, """
        <html>
          <head>
            <title>Today's News</title>
          </head>
          <body>
          <h1>Today's News</h1>
        """

        print >> out, '<ul>'
        id = 0
        for item in items:
            id += 1
            print >> out, '  <li><a href="#%i">%s</a></li>' % (id, item.title)
        print >> out, '</ul>'

        id = 0
        for item in items:
            id += 1
            print >> out, '<h2><a name="%i">%s</a></h2>' % (id, item.title)
            print >> out, '<pre>%s</pre>' % item.body

        print >> out, """
          </body>
        </html>
        """

def runDefaultSetup():
    """
    A default setup of sources and destination. Modify to taste.
    """
    agent = NewsAgent()

    # A SimpleWebSource that retrieves news from the BBC News site:
    bbc_url = 'http://news.bbc.co.uk/text_only.stm'
    bbc_title = r'(?s)a href="[^"]*">\s*<b>\s*(.*?)\s*</b>'
    bbc_body = r'(?s)</a>\s*<br />\s*(.*?)\s*<'
    bbc = SimpleWebSource(bbc_url, bbc_title, bbc_body)

    agent.addSource(bbc)

    # An NNTPSource that rerieves news from comp.lang.python.anounce:
    #clpa_server = 'news.kornet.net'
    #clpa_group = 'comp.lang.python.announce'
    #clpa_window = 1
    #clpa = NNTPSource(clpa_server, clpa_group, clpa_window)
    ht_server = 'news.kornet.net'
    ht_group = 'han.test'
    ht_window = 1
    ht = NNTPSource(ht_server, ht_group, ht_window)

    #agent.addSource(clpa)
    agent.addSource(ht)

    # Add plain-text destination and an HTML destination:
    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    # Distribute the news items:
    agent.distribute()

if __name__ == '__main__':
    runDefaultSetup()
