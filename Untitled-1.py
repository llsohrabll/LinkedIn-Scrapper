import openpyxl

with open('ExtractedNames.txt', 'r', encoding='utf-8') as file:
    names = file.readlines()

with open('ExtractedJob.txt', 'r', encoding='utf-8') as file:
    jobs = file.readlines()

names = [name.strip() for name in names]
jobs = [job.strip() for job in jobs]

file_name = 'ExtractedData.xlsx'

# بررسی اگر فایل اکسل موجود بود، آن را بارگذاری کنیم و در غیر این صورت فایل جدید بسازیم.
try:
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
except FileNotFoundError:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Job"])

# بررسی که اگر لینکدین ممبر باشد، فقط آخرین شغل وارد نشود
last_added = False  # این متغیر برای شناسایی اینکه آخرین شغل وارد شده است یا نه استفاده می‌شود.

for name, job in zip(names, jobs):
    if "LinkedIn Member" in name and not last_added:  # اگر "LinkedIn Member" در نام باشد و شغل آخر هنوز وارد نشده باشد
        last_added = True  # پس از این شغل، وارد کردن شغل آخر متوقف می‌شود
        continue  # از وارد کردن این شغل صرف نظر کن
    elif last_added:
        last_added = False  # پس از نادیده گرفتن شغل آخر، وارد کردن داده‌ها از سر گرفته می‌شود
        continue
    else:
        ws.append([name, job])  # نام و شغل را اضافه کن

# ذخیره فایل اکسل
wb.save(file_name)
print(f"Data has been saved to '{file_name}'.")
