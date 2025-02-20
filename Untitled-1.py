import openpyxl

with open('ExtractedNames.txt', 'r', encoding='utf-8') as file:
    names = file.readlines()

with open('ExtractedJob.txt', 'r', encoding='utf-8') as file:
    jobs = file.readlines()

names = [name.strip() for name in names]
jobs = [job.strip() for job in jobs]

file_name = 'ExtractedData.xlsx'

try:
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
except FileNotFoundError:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Job"])

last_added = False  

for name, job in zip(names, jobs):
    if "LinkedIn Member" in name and not last_added:  
        last_added = True  
        continue 
    elif last_added:
        last_added = False 
        continue
    else:
        ws.append([name, job])  

wb.save(file_name)
print(f"Data has been saved to '{file_name}'.")
