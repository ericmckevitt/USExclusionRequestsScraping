from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/325609'
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

table = soup.find('table', class_="portstable")
print(f"table: {table}")