import pdfkit

url = 'https://what-if.xkcd.com/'
l=[]
for i in range(1,5):
    l.append(url + str(i) + '/')

pdfkit.from_url(['https://what-if.xkcd.com/1/','https://what-if.xkcd.com/2/'], 'out.pdf')