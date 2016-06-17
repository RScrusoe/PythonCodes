import re
import requests

while(1):
    try:
        word=input("Enter any word ")
        url = "http://dictionary.reference.com/browse/" + word
        data = requests.get(url).text
        m = re.search('<div class="def-content">',data)
        if(m==None):
            print("Couldn't find the meaning\n ")
            continue
        start = m.end()

        data2 = data[start:(start+500)]
        m = re.search('<',data2)
        new_start = m.start()
        print(data2[:new_start])
        print('')
    except:
        print("Couldn't find the meaning ")
