from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/325609'
options = ChromeOptions()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

table = soup.find('table', class_="portstable")
print(f"table: {table}")

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("http://www.python.org")

# driver.close()