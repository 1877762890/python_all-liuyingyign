import xlrd
'''
   1.安装与导入xlrd模块（读取excel）

'''
data=xlrd.open_workbook("E:\\测试开发\\a.xlsx")

# 2.从工作簿里选中选项卡
sheet=data.sheet_by_name("用户管理")

# 3.
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows=sheet.nrows
cols=sheet.ncols
for i in range(rows):
    for j in range(cols):
        print(str(sheet.cell_value(i,j)).replace(".0",""),"\t",end="")
    print()












