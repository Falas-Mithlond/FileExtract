
import tkinter
import os


class Test(tkinter.Frame):

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.path = tkinter.Label(frame, text='path')
        self.path.grid(row=0, column=0)
        self.ent = tkinter.Entry(frame)
        self.ent.grid(row=0, column=1)
        self.submit = tkinter.Button(frame, text='submit', command=self.Print)
        self.submit.grid(row=1, column=1)
        self.result = tkinter.Label(frame, text='')
        self.result.grid(row=2, column=0)

    def Print(self):
        s = self.ent.get()
        self.result['text'] = s
        self.ent.delete(0, len(s))

root = tkinter.Tk()
root.geometry('700x300')
root.title('硅钢冲剪题目抽取')
app = Test(root)

# if __name__ == "__main__":
#     root.mainloop()
