from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import regex
import openpyxl
a
os.system("cls")

EMAIL = '****'
PASSWORD = '****'

company_url = input("\n\nPlease Enter Main Page of Company\nFor Example ---> https://www.linkedin.com/company/google/\n\n---> ")

driver = webdriver.Chrome()

try:
    driver.get('https://www.linkedin.com/login')
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(EMAIL)

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    time.sleep(20)

    driver.get(company_url)
    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    page_html = driver.page_source

    with open('CleanData.txt', 'w', encoding='utf-8') as file:
        file.write(page_html)

    print("HTML source has been saved to 'CleanData.txt'")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()


with open('CleanData.txt', 'r', encoding='utf-8') as file:
    page_html = file.read()

person_pattern = r"[\p{L}_][\p{L}_\s]*(?:\([^\)]*\))*(?=\s*(?:’|')s?\s+profile\s+picture)"
#person_pattern = r"[A-Za-z][a-zA-Z]*(?:\s+[A-Za-z][a-zA-Z]*|\s*\([^\)]*\))*(?=\s*(?:’|')?s\s+profile\s+picture)"
person_matches = regex.findall(person_pattern, page_html)

with open('ExtractedNames.txt', 'w', encoding='utf-8') as output_file:
    for match in person_matches:
        output_file.write(match + '\n')

print(f"\nExtracted Names have been saved to 'ExtractedName.txt'.")

job_pattern= r'style="-webkit-line-clamp: 2">\s*\n\s*(.*)'
job_matches = regex.findall(job_pattern, page_html)

with open('ExtractedJob.txt', 'w', encoding='utf-8') as output_file:
    for match in job_matches:
        output_file.write(match + '\n')

print(f"\nExtracted jobs have been saved to 'ExtractedJob.txt'.")

# EXCEL #

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

for name, job in zip(names, jobs):
    ws.append([name, job])

wb.save(file_name)
print(f"Data has been saved to '{file_name}'.")


