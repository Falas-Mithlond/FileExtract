
import os
import xlrd
import random
import tkinter


class problemDis(tkinter.Frame):

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.pathLab = tkinter.Label(frame, text='文件路径')
        self.pathLab.grid(row=0, column=0)

        self.path = tkinter.Entry(frame)
        self.path.grid(row=0, column=1)

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
        respath = self.output.get()
        if not os.path.exists(source):
            self.error['text'] = '文件路径 {} 不存在'
        else:
            data = xlrd.open_workbook(source)

        problemDis.judgeTable(self, data, respath)
        problemDis.radioTable(self, data, respath)
        problemDis.checkTable(self, data, respath)

    
    def judgeTable(self, data, respath):
        judgeTab = data.sheet_by_name('判断题')
        judgeRow = judgeTab.nrows
        judgeCol = judgeTab.ncols
        judgeNum = int(self.judge.get())
        judgeList = random.sample(range(judgeRow-3), judgeNum)
        judgedatas = []
        for i in range(3, judgeRow):
            judge_sheet = []
            for j in range(judgeCol):
                judge_ctype = judgeTab.cell(i, j).ctype
                judge_cell = judgeTab.cell_value(i, j)
                if judge_ctype == 2 and judge_cell % 1 == 0:
                    judge_cell = int(judge_cell)
                judge_sheet.append(judge_cell)
            judgedatas.append(judge_sheet)
        f = open(respath, 'a')
        f.write('判断题 \n')
        for i in judgeList:
            s = str(judgedatas[i]).replace('[','').replace(']','')
            s = s.replace("'", '').replace(',', '')+'\n'
            f.write(s)
        f.close()
        
    def radioTable(self, data, respath):
        radioTab = data.sheet_by_name('单选择题')
        radioRow = radioTab.nrows
        radioCol = radioTab.ncols
        radioNum = int(self.radio.get())
        radioList = random.sample(range(radioRow-3), radioNum)
        radiodatas = []
        for i in range(3, radioRow):
            radio_sheet = []
            for j in range(radioCol):
                radio_ctype = radioTab.cell(i, j).ctype
                radio_cell = radioTab.cell_value(i, j)
                if radio_ctype == 2 and radio_cell % 1 == 0:
                    radio_cell = int(radio_cell)
                radio_sheet.append(radio_cell)
            radiodatas.append(radio_sheet)
        f = open(respath, 'a')
        f.write('\n 单选题 \n')
        for i in radioList:
            s = str(radiodatas[i]).replace('[','').replace(']','')
            s = s.replace("'", ' ').replace(',', ' ')+'\n'
            f.write(s)
        f.close()
    
    def checkTable(self, data, respath):
        checkTab = data.sheet_by_name('多选题')
        checkRow = checkTab.nrows
        checkCol = checkTab.ncols
        checkNum = int(self.check.get())
        checkList = random.sample(range(checkRow-3), checkNum)
        checkdatas = []
        for i in range(3, checkRow):
            check_sheet = []
            for j in range(checkCol):
                check_ctype = checkTab.cell(i, j).ctype
                check_cell = checkTab.cell_value(i, j)
                if check_ctype == 2 and check_cell % 1 == 0:
                    check_cell = int(check_cell)
                check_sheet.append(check_cell)
            checkdatas.append(check_sheet)
        f = open(respath, 'a')
        f.write('\n 多选题 \n')
        for i in checkList:
            s = str(checkdatas[i]).replace('[','').replace(']','')
            s = s.replace("'", ' ').replace(',', ' ')+'\n'
            f.write(s)
        f.close()

root = tkinter.Tk()
root.geometry('700x300')
root.title('题目抽取')
app = problemDis(root)

if __name__ == "__main__":
    root.mainloop()
