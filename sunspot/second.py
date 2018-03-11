#! -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

from urllib import urlopen

#URL='http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt'
URL='http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS='#:'

#Y_OFFSET=40
Y_OFFSET=0

#X_OFFSET=2007
X_OFFSET=2017

OUTPUT_FILE='report2.pdf'

data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        print("Adding %s" % [float(n) for n in line.split()])
        data.append([float(n) for n in line.split()])

print("Data retrieved : %s" % data)

drawing = Drawing(200, 150)

pred = [row[2]-Y_OFFSET for row in data]
print("Predictions : %s" % pred)
high = [row[3]-Y_OFFSET for row in data]
print("High : %s" % high)
low = [row[4]-Y_OFFSET for row in data]
print("Low : %s" % low)
times = [200*((row[0] + row[1]/12.0) - X_OFFSET)-110 for row in data]
print("Times : %s" % times)

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), stokeColorr=colors.green))

drawing.add(String(65, 115, u'썬쓰빳츠', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, OUTPUT_FILE, 'Sunspots')
