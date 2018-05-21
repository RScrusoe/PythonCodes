from tkinter import *

root = Tk()

top = Frame(root)
top.pack()

bottom = Frame(root)
bottom.pack()

b1 = Button(top,text="b1",fg='red')
b2 = Button(top,text="b2",fg='magenta')
b3 = Button(bottom,text="b3",fg='purple')
l1 = Label(root,text="Crusoe!",bg='white',fg='black')

b1.pack(side=RIGHT)
b2.pack(side=LEFT)
b3.pack(side=BOTTOM)
l1.pack(fill=X)



root.mainloop()