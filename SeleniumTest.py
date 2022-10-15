from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup 

options = ChromeOptions()
options.add_argument("--headless")

# Make a Chrome driver
driver = webdriver.Chrome(executable_path='/Users/ericmckevitt/Documents/chromedriver', options=options)

# Get the page
driver.get('https://232app.azurewebsites.net/Forms/ExclusionRequestItem/325609')

# Get the HTML
html = driver.page_source

# Close the driver
driver.close()

# Print the HTML
print(html)

soup = BeautifulSoup(html, 'lxml')

# Find table with class name = "portstable"
class_name = "portstable"
table = soup.find('table', class_=class_name)
print(f"\n\n\n---------------\n\n\ntable: {table}")