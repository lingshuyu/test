from tkinter import *

def callback():
    var.set('吹吧你，我才不信喃')

root= Tk()

frame1=Frame(root)
frame2=Frame(root)

var=StringVar()
var.set('你所下载的影像有问题\n请稍后在点击')

textLabel=Label(frame1,
                textvariable=var,
                justify=LEFT,
                padx=10)
textLabel.pack(side=LEFT)

photo=PhotoImage(file='1.gif')
imgLabel=Label(root,image=photo)
imgLabel.pack(side=RIGHT)

theButton=Button(frame2,text='我已解决',command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()