
import os
import xlrd
import tkinter

class InterFace(tkinter.Frame):
    
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.pathLab = tkinter.Label(frame, text='文件路径')
        self.pathLab.grid(row=0, column=0, sticky='W')
        self.path = tkinter.Entry(frame)
        self.path.grid(row=0, column=1, sticky='W')

        self.judLab = tkinter.Label(frame, text='判断题数')
        self.judLab.grid(row=1, column=0, sticky='W')
        self.judge = tkinter.Entry(frame)
        self.judge.grid(row=1, column=1, sticky='W')

        self.radioLab = tkinter.Label(frame, text='单选题数')
        self.radioLab.grid(row=2, column=0, sticky='W')
        self.radio = tkinter.Entry(frame)
        self.radio.grid(row=2, column=1, sticky='W')

        self.checkLab = tkinter.Label(frame, text='多选题数')
        self.checkLab.grid(row=3, column=0, sticky='W')
        self.check = tkinter.Entry(frame)
        self.check.grid(row=3, column=1, sticky='W')

        self.outputLab = tkinter.Label(frame, text='输出路径')
        self.outputLab.grid(row=4, column=0, sticky='W')
        self.output = tkinter.Entry(frame)
        self.output.grid(row=4, column=1, sticky='W')

        self.submit = tkinter.Button(frame, text='提交', command=self.readExcel)
        self.submit.grid(row=5, columnspan=2)

        self.error = tkinter.Label(frame, text='')
        self.error.grid(row=6, columnspan=2)
    
    def readExcel(self):
        source = self.path.get()
        if not os.path.exists(source):
            self.error['text'] = '文件路径 {} 不存在'
        else:
            self.data = xlrd.open_workbook(source)