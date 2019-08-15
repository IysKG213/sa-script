import shutil, os, re, datetime, pprint, openpyxl as excel

# 入力対象
file_invoice= '各社作業実績管理_2019年07月度_3.xlsx'

os.chdir('C:\\Users\\d043528\\Desktop\\Markdown')
files = []

# 入力対象ファイルを読む
wb_iv = excel.load_workbook(file_invoice)
sheet = wb_iv['各社作業実績工数表 (2019年7月)'] 

# 入力先のセルと値
sheet['G10'] = 50
sheet['H10'] = 30
sheet['I10'] = 30
sheet['O10'] = 20
sheet['P10'] = 1.5

# 保存する
wb_iv.save(file_invoice)
print('ok')