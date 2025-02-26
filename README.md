# LinkedIn Data Scraper

This Python script uses Selenium to scrape data from LinkedIn company pages. It logs into LinkedIn with provided credentials, navigates to a specified company's main page, scrolls to load all employees, saves the HTML source to a file, and extracts relevant data into an Excel spreadsheet.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (included for Chrome browser automation)
- `openpyxl` library for Excel file handling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/llsohrabll/LinkedIn-Scrapper
   cd LinkedIn-Scrapper
   ```

2. Install dependencies:
   ```bash
   pip install selenium openpyxl
   ```

3. Download Chrome WebDriver:
   - Visit [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) and download the appropriate version for your Chrome browser.

4. Place the `chromedriver.exe` in the same directory as your script.

## Usage

1. Run the script:
   ```bash
   python linkedin_scraper.py
   ```

2. Follow the prompts to enter your LinkedIn credentials and the company's main page URL.

3. After execution, the script will generate an `output.xlsx` file containing extracted data.

## Notes

- Ensure that you comply with LinkedIn's terms of service and data usage policies when using this script.
- This script assumes you have a valid LinkedIn account and proper permissions to access the company's page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

