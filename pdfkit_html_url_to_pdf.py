import pdfkit

#pdfkit.from_url(['http://www.feynmanlectures.caltech.edu/I_01.html','http://www.feynmanlectures.caltech.edu/I_02.html','http://www.feynmanlectures.caltech.edu/I_03.html'], 'out.pdf')
pdfkit.from_url(['google.com', 'yahoo.com', 'http://fb.com'], 'out.pdf')
pdfkit.from_file('test.html', 'out.pdf')