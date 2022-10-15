from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

url = 'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/325609'

s = HTMLSession()
response = s.get(url)
response.html.render()

html = response.html.html

soup = BeautifulSoup(html, 'html.parser')

# Send a request, but wait for the page to load so the JS can run
r = requests.get(url, timeout=5, verify=False, stream=True)
r.raw.decode_content = True
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')

# Find table with class name = "portstable"
class_name = "portstable"
table = soup.find('table', class_=class_name)
print(f"table: {table}")

