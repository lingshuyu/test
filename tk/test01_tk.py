import tkinter as tk

class APP:
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=20,pady=20)

        self.hi_there=tk.Button(frame,text="打招呼",fg="blue",command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("互联网的广大朋友们大家好啊")

root=tk.Tk()
app=APP(root)

root.mainloop()