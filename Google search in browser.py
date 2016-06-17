import webbrowser
lib=input("Enter what you want to search for:")
ur="https://www.google.co.in/search?q="
webbrowser.open_new(ur+lib)


'''# using google module
from google import search
for url in search('iitb', stop=20):
    print(url)
'''