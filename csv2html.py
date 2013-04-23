#-*- coding: utf-8 -*-

import sys
import unicodecsv as csv

filename = sys.argv[1]
c = filename.split('.')[:-1]
c.append('html')
out = '.'.join(c)

outf = open(out, 'wb')

outf.write('<html>')
outf.write('<body>')
outf.write('<table border="1" >')

with open(filename, 'rb') as f:
    reader = csv.reader(f, encoding='utf-8', delimiter='\t')
    for row in reader:
        outf.write('<tr>')
        for value in row:
            outf.write('<td>')
            v = value 
            if value.startswith('http://') or value.startswith('https://') or value.startswith('www.'):
                v = '<a href="%s">%s</a>' % (value, value, )
            outf.write(v.encode('utf-8'))
            outf.write('</td>')
        outf.write('</tr>')

outf.write('</table>')
outf.write('</body>')
outf.write('<html>')

