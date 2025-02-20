import re
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(["Name", "Next Line After Tag"])

html_file_path = r'C:\Users\Dotin\Desktop\CleanData.txt'

with open(html_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        
        match_profile = re.search(r'View (.*?)’s profile', line)
        if match_profile:
            name = match_profile.group(1).strip()  
            ws.append([name, ""])  

        if '<!----><!----></div>' in line:
            if i + 4 < len(lines):
                next_line = lines[i + 4].strip()
                ws.append(["", next_line])  
wb.save(r"C:\Users\Dotin\Desktop\output.xlsx")
