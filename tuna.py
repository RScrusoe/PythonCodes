import random
import urllib.request


def fish():
    print("I'm tuna fish")

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

    # call this    tuna.download_image("url of img")
#----------------------------------------------------------------


# to read and write file

fw = open('sample.txt', 'w')
fw.write("hey there\nwhats up??\n")
fw.close()

fr=open('sample.txt', 'r')
name = fr.read()

print(name)


#-----------------------------------------------------------------------

        #### For ERROR HANDLING

while True:
    try:
        number = int(input("Enter any number "))
        print(36/number)
        break
    except ValueError:
        print("Enter a number only")
    except ZeroDivisionError:
        print("Dont enter zero")

    except:
        print("you suck")
    finally:
        print("DONE!!!!!!!!!!")

##--------------------------------------------------------------------------------

    ### TURTLE

import turtle

def square():
    window = turtle.Screen()
    window.bgcolor("yellow")
    brad = turtle.Turtle()
    for x in range(1,24):

        brad.forward(120)
        brad.right(90)
        brad.forward(120)
        brad.right(90)
        brad.forward(120)
        brad.right(90)
        brad.forward(120)
        brad.right(90)
        brad.right(15)


    window.exitonclick()


square()


##-------------------------------------------------------------------------

            ## CLASS & INHERITANCE EXAMPLE
class Enemy():

    def __init__(self,x):
        self.life = x
        print("Enemy boject of life " + str(self.life)+ " created")
    def attack(self):
        self.life -= 1
        print("ohhhh")

    def CheckLife(self):
        print(self.life)


class ChildEnemy(Enemy):
    def __init__(self,x):
        self.life = x
        print("ChildEnemy boject of life " + str(self.life)+ " created")
    def name(self):
        print("Im child enemy")

matt = Enemy(10)

matt.attack()
matt.CheckLife()


maty = ChildEnemy(2)
maty.name()



#--------------------------------------------------------------------


            ## THREADING EXAMPLE

import threading
class timer(threading.Thread):
    def run(self):
        for x in range(10):
            print(str(x) + ' in clock ' + threading.currentThread().getName())

           # print('\n')

one = timer(name="11111111")
two = timer(name="22222222")
one.start()
two.start()



#----------------------------------------------------------------------------
            ## ZIP SORT MAX MIN

stocks = {
    'Rahul':5, 'Rohan':8,
    'Vishal':5, 'Shray':7,
    'Uday':9
}

print(sorted(zip(stocks.values(),stocks.keys())))


#---------------------------------------------------------------------------

        ## BUTTONS


from tkinter import *
root =Tk()
addLabel = Label(root,text= "HELL000")
addLabel.pack()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame()
bottomFrame.pack()


button1 = Button(topFrame, text="B1", fg= 'red')
button2 = Button(topFrame, text = "B2", fg = "Blue")
button3 = Button(bottomFrame, text = "B3", fg = "yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)



root.mainloop()


#----------------------------------------------------------------------

        ## GRID

from tkinter import *
root =Tk()

def myName(event):
    print("My name is Crusoe!!")


label1 = Label(root, text="Name")
label2 = Label(root, text="Password")

entry1 = Entry(root)
entry2 = Entry(root)

c= Checkbutton(root,text="Keep me logged in")
c.grid(row=2,columnspan = 2)

label1.grid(row=0, sticky=E)
label2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1 = Button(root, text="my name is..")
button1.grid(row=4,columnspan=2)

button1.bind("<Button-1>",myName)

root.mainloop()


#---------------------------------------------------------------------------

        ## FIBONACCI SERIES

a,b = 0,1
out = open('fibonacci.txt','w')

while b<1000:
    a, b = b, a+b
    out.write(str(b))
    out.write("\n")

out.close()

#----------------------------------------------------------------------------


                    ## search, replace

import re
inf = open('a.txt')
'''
for line in inf:
    if re.search('it',line):
        print(line)

for line in inf:
    print(re.sub('it','@@@@@@@@@@@@@@@@@@@@@@@@@',line))
'''

for line in inf:
    match = re.search('I',line)
    if match:
        print(line.replace(match.group(),'@@@@@@@@@@@@@@@@@@@'),end="")



#--------------------------------------------------------------------

            ##args, inclusive function



def inclusive_range(*args):
    arglen = len(args)
    if arglen < 1: raise TypeError("requiress at least 1 argument")
    elif arglen == 1:
        start = 0
        step = 1
        stop = args[0]
    elif arglen == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif arglen == 3:
        start =args[0]
        stop = args[1]
        step = args[2]
    else: raise TypeError("at most 3 arguments are allowed")
    i = start
    while i<=stop:
        yield i
        i+=step




for i in inclusive_range(25):
    print(i,end=" ")


#--------------------------------------------------------

        ## args kwrgs




def testfun(this, that, other, *args, **kwrgs):
    print(
        this, that, other, end=" ")
    for i in args:
        print(i, end=" ")
    print(kwrgs['one'], kwrgs['two'], kwrgs['seven'], end=" ")


testfun(1,2,3,8,9,10,one = 1, two =123 , seven = 17)



##---------------------------------------------------------------

            ##Class : set variables / get variables

class Duck:
    def __init__(self,**kwargs):
        self.variables = kwargs
    def quack(self):
        print("Quackk , Quackk!!!")

    def set_variable(self,k,v):
        self.variables[k] = v
    def get_variable(self,k):
        return self.variables.get(k ,None)
Donald = Duck(color='blue')
print(Donald.get_variable('color'))
Donald.set_variable('color','red')
Donald.set_variable('feet','2')
print(Donald.get_variable('color'))
print(Donald.get_variable('feet'))



#------------------------------------------------------------------------

        ## Strings

s="My name is Crusoe !"

a = ', '.join(s.split())
print(a)
print('@'.join('I love Physics'.split()))

print("#" + ' #'.join("chouka choukat golibar dhad dhud dhad dhud".split()))
q="this is {} a string"
print(id(q))
print(id(q.format(1)))

d= dict(bob = 'x', fred ='x', Rasi = 'z' )
print("This is {bob} , that is {Rasi} ".format(**d))



#------------------------------------------------------------------------------



        ##html to txt

import os
import sys
import urllib.request
print("Python version {}.{}.{} ".format(*sys.version_info))
print(sys.platform)
print(os.name)
page = urllib.request.urlopen('file:///C:/Users/RS%20Rahul/OneDrive/Documents/My%20Python%20codes/help.html')
outf = open('help_copy.txt','w')
for l in page:
    x=str(l,encoding='utf_8')
    outf.write(x)

#----------------------------------------------------------------------------------

        ## Random number to month
import csv

with open('test.csv') as csvfile:
    readHere = csv.reader(csvfile, delimiter=",")
    num1 = input("Enter random number less than hundred   :   ")
    diff = []
    for row in readHere:
        diff.append(abs(int(num1) - int(row[3])))
    index = diff.index(min(diff))


with open('test.csv') as inf:
    readHereAgain = csv.reader(inf, delimiter=",")
    list =[]
    for asd in readHereAgain:
        list.append(asd[1])
    print(list[index])


#-----------------------------------------------------------
        ##Prime Numbers
outfile = open("primes.txt",'w')
for num in range(2,10000000):

    for i in range(2,int(num**0.5)):
        if num%i==0:
            break
    else:
        outfile.write(str(num)+'\n')

outfile = open("primes.txt",'w')
list=[]
for num in range(2,100000):

    for i in list:
        if num%i==0:
            break
    else:
        list.append(num)
        outfile.write(str(num)+'\n')

#------------------------------------------------------------------------------------------------

##  ADDING USER AGENT

import urllib
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))


##########################################################################################

#Random user agent:

from random import choice
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]


print(choice(user_agents))



##################################################################################################

#                   CLASS


class Employee:
    'This is Employee class'

    ct = 0
    def __init__(self,name,salary):
        Employee.ct +=1
        self.name = name
        self.salary = salary

    def display_count(self):
        #print("hi")
        print("Total Employees : " + str(Employee.ct))
    def display_employee(self):
        print(self.name + '  ' + str(self.salary))


e1 = Employee('Zara' , 15000)
e2 = Employee ('sam', 20000)
e1.display_employee()
e2.display_employee()
Employee.display_count(Employee)
e1.age = 18
print(e1.age)
print(hasattr(e2,'age'))
setattr(e2,'age',22)
print(getattr(e2,'age'))
print(Employee.__module__)



class Vector:
    def __init__(self, a, b):
        print('creating vector')
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)
