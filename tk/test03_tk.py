from tkinter import *

root= Tk()

photo=PhotoImage(file='1.gif')
theLabel=Label(root,
               text='学python',
               justify=LEFT,
               image=photo,
               compound=CENTER,
               font=('华康少女字体',20),
               fg='yellow')
theLabel.pack()
mainloop()