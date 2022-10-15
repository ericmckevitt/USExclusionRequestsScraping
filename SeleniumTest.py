from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup 
from lxml import etree

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
print(f"\n\n\n------------00---\n\n\ntable: {table} \n {type(table)}")
print("\n\n", table.findChildren('tr'))
children = table.findChildren('tr')
for i, child in enumerate(children):
    print(f"\nchild {i}: {child}")
    # Get the text of the child
    child_text = child.text
    print(f"\tchild_text: {child_text}")


# dom = etree.HTML(str(soup))

# # Find table with class name = "portstable"
# xpath = "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[9]/div[2]/table"
# table = dom.xpath(xpath)[0]
# print(f"\n\n\n---------------\n\n\ntable: {table}")

# Get the table's children
