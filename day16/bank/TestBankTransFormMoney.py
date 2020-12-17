import xlrd
class TransFromeMoney:
    @classmethod
    def read(cls,filename="",sheetname="0"):
        try:
            list=[]
            file = xlrd.open_workbook(filename,)
            if sheetname.isdigit():
                sheet = file.sheet_by_index(int(sheetname))
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
            else:
                sheet = file.sheet_by_name(sheetname)
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
            return list
        except Exception as error:
            print(error)
# n=TransFromeMoney.read("D:\\pythonProject1\\day16\\bank\\b.xlsx","Sheet1")
# print(n)









