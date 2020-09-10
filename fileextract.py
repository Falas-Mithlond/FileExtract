import xlrd
import random

class ExcelData():
    def __init__(self, data_path, sheetname):
        self.data_path = data_path
        self.sheetname = sheetname
        self.data = xlrd.open_workbook(self.data_path)
        self.table = self.data.sheet_by_name(self.sheetname)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def readExcel(self):
        datas = []
        for i in range(3, self.rowNum):
            sheet_data = []
            for j in range(self.colNum):
                c_type = self.table.cell(i, j).ctype
                c_cell = self.table.cell_value(i, j)
                if c_type == 2 and c_cell % 1 == 0:
                    c_cell = int(c_cell)
                sheet_data.append(c_cell)
            datas.append(sheet_data)
        return datas

# if __name__ == "__main__":
#     data_path = "硅钢片冲剪工-初级1.xls"
#     sheetname = "判断题"
#     get_data = ExcelData(data_path, sheetname)
#     datas = get_data.readExcel()
#     length = 5
#     label = random.sample(range(100), length)
#     textname = "test2.txt"
#     f = open(textname, "a")
#     for i in label:
#         s = str(datas[i]).replace('[','').replace(']','')
#         s = s.replace("'", ' ').replace(',', '') + '\n'
#         f.write(s)
#     f.close()
