import pdfkit

url = 'https://what-if.xkcd.com/'
l=[]
for i in range(1,157):
    urll = url + str(i) + '/'
    name = str(i) + '.pdf'
    pdfkit.from_url(urll, name)