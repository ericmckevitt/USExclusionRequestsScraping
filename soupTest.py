from bs4 import BeautifulSoup
import requests
from lxml import etree

id = 324372
url = f'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/{id}'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'breadcrumbroot=Home; ARRAffinity=72af3dfa41ff3cc38aff5a6337ecd95be559debaba0407db4dff2ec455824ddb; ARRAffinitySameSite=72af3dfa41ff3cc38aff5a6337ecd95be559debaba0407db4dff2ec455824ddb; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8DVULPx4GftJklCVHrG7iQcIO-evQRot4Y4rjubVAUmawjQmZ_bMWlGCEi5R3Ql2_R9ECCIruSacjCT6QicPOeOanSP_ba6C2ig4nDaNYSkHLFoWFK4R7mHBoEEjXmY9HeYXA4uIee5qWKYsLZKTEkM',
    'Host': '232app.azurewebsites.net',
    'Pragma': 'no-cache',
    'Referer': 'https://232app.azurewebsites.net/Index',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',

    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "html.parser")
# print(soup.prettify())

dom = etree.HTML(str(soup))
xpath = '/html/body/div[2]/div/div/form/div/div[2]/h3[2]'
print('\n\n\n')
# print(dom.xpath(f'{xpath}')[0].text)

xpath = '/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/input'
print("Identify the Activity:", dom.xpath(f'{xpath}')[0].get('value'))

xpath = '/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/input'
print("Identify the Organization:", dom.xpath(f'{xpath}')[0].get('value'))

xpath = '/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/input'
print("Identify the country where the organization is headquartered:",
      dom.xpath(f'{xpath}')[0].get('value'))

xpath = '/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[3]/textarea'
print("Comments:", dom.xpath(f'{xpath}')[0].text)

xpath = '/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/div/input'
print("Identify the primary type of activity of the Exclusion Requester:",
      dom.xpath(f'{xpath}')[0].get('value'))
