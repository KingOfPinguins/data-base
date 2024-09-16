import pandas as pd
import glob
import openpyxl

# Specify the path to the folder containing the Excel files
folder_path = 'D:\\WORK\\PROJECTS\\DB\\res\\'

# List all Excel files in the folder
all_files = glob.glob(folder_path + "*.xlsx")

print("files:", all_files)


counter = 1
phones = []
for i in all_files:
    workbook = openpyxl.load_workbook(i)
    sheet = workbook.active
    print("WORK ", i)
    
    
    
    for row in sheet.iter_rows(values_only=True):
        try:
            if "+1" in str(row):
                line = str(row).split(',')
                for y in line:
                    if "+1" in str(y):
                        phones.append('+1 ' + y.split(' ')[-1].replace('\'', ''))
        except:
            pass

phones = list(set(phones))
    
with open('.numbers.txt', '+a') as file_m:
    for phone in phones:
        file_m.write(str(phone).replace(' ', '').replace('-', '') + '\n')


print(phones)
print("LENTH:", len(phones))