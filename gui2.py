from tkinter import *

root = Tk()

l1 = Label(root,text="Name")
l2 = Label(root,text="Password")
e1 = Entry(root)
e2 = Entry(root)
c1 = Checkbutton(root,text='Keep me signed in')

l1.grid(row=0,sticky=E)
l2.grid(row=1)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
c1.grid(columnspan=2)


root.mainloop()
52jxtszde7