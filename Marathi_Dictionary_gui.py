from bs4 import BeautifulSoup

import urllib.request

import urllib
from tkinter import *


from random import choice

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]



def make_soup(url):
    req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': choice(user_agents)
    }
    )
    data = urllib.request.urlopen(req)
    soup = BeautifulSoup(data,'html.parser')
    return soup




def Dict(event):
    word = entry.get()
    url = 'http://www.shabdkosh.com/mr/translate?e=' + word +'&l=mr'
    soup = make_soup(url)
    meaning = ''
    for i in soup.findAll('a',{'class':'in l'}):

        meaning = meaning +'\n' + i.get_text()
    res.configure(text = "Meaning: " + meaning)


w = Tk()
Label(w, text="Enter Word:").pack()
entry = Entry(w)
entry.bind("<Return>", Dict)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()




