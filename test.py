
import xlrd
from xlrd import xldate_as_tuple


class ExcelData():
    def __init__(self, data_path, sheetname):
        self.data_path = data_path
        self.sheetname = sheetname
        self.data = xlrd.open_workbook(self.data_path)
        self.table = self.data.sheet_by_name(self.sheetname)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def readExcel(self):
        datas = []
        for i in range(1, self.rowNum):
            sheet_data = {}
            for j in range(self.colNum):
                c_type = self.table.cell(i, j).ctype
                c_cell = self.table.cell_value(i, j)
                if c_type == 2 and c_cell % 1 == 0:
                    c_cell = int(c_cell)
                sheet_data[self.keys[j]] = c_cell
            datas.append(sheet_data)
        return datas


# if __name__ == "__main__":
#     data_path = "门户集成系统.xlsx"
#     sheetname = "Sheet1"
#     get_data = ExcelData(data_path, sheetname)
#     datas = get_data.readExcel()
#     print(datas)
