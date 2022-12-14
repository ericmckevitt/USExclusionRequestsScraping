from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup 
import requests
import pprint
import pandas as pd
from lxml import etree
import cleanData as cd

DEBUG = False

num_records = 3

url = 'https://232app.azurewebsites.net/Index?handler=SummaryView'

# Filters
ID = ''
COMPANY_NAME = ''
PRODUCT = ''
HTSUSCode = '721933'  # 721933 or 721932
PUBLIC_STATUS = ''
WINDOW_CLOSE = ''
PUBLISH_DATE = ''

payload = {"draw": 1, "columns": [{"data": 0, "name": "ID", "searchable": True, "orderable": True, "search": {"value": f"{ID}", "regex": False}},
                                    {"data": 1, "name": "Company", "searchable": True, "orderable": True, "search": {
                                        "value": f"{COMPANY_NAME}", "regex": False}},
                                    {"data": 2, "name": "Product", "searchable": True, "orderable": True, "search": {
                                        "value": f"{PRODUCT}", "regex": False}},
                                    {"data": 3, "name": "HTSUSCode", "searchable": True, "orderable": True, "search": {
                                        "value": f"{HTSUSCode}", "regex": False}},
                                    {"data": 4, "name": "PublicStatus",
                                    "searchable": True, "orderable": True, "search": {"value": f"{PUBLIC_STATUS}", "regex": False}},
                                    {"data": 5, "name": "WindowClose", "searchable": True,
                                        "orderable": True, "search": {"value": f"{WINDOW_CLOSE}", "regex": False}},
                                    {"data": 6, "name": "PublishDate", "searchable": True,
                                        "orderable": True, "search": {"value": f"{PUBLISH_DATE}", "regex": False}},
                                    {"data": 7, "name": "", "searchable": True, "orderable": False, "search": {"value": "", "regex": False}}],
            "order": [{"column": 0, "dir": "desc"}], "start": 0, "length": num_records, "search": {"value": "", "regex": False}}


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '912',
    'Content-Type': 'application/json',
    'Cookie': 'breadcrumbroot=Home; ARRAffinity=72af3dfa41ff3cc38aff5a6337ecd95be559debaba0407db4dff2ec455824ddb; ARRAffinitySameSite=72af3dfa41ff3cc38aff5a6337ecd95be559debaba0407db4dff2ec455824ddb; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8DVULPx4GftJklCVHrG7iQfo3OWfuzrbLkPVdHOdloOD0z9KwLw3NcS_7zbJE6rTbEqZa4YsRqRpy9Tlvu0e_rXuFTxvJhtMO-_c7ocUA0Rnplj1ozHV4FSzScDZ4e3Ih2JoWnvJQDd6AtzI47UR8-0',
    'Host': '232app.azurewebsites.net',
    'Origin': 'https://232app.azurewebsites.net',
    'Pragma': 'no-cache',
    'Referer': 'https://232app.azurewebsites.net/Index',
    'RequestVerificationToken': 'CfDJ8DVULPx4GftJklCVHrG7iQf0nzZsCkc6cB2zjeKlhjAzcZlvjd5RO7bEF75kIatavEiSoRD90bkQXiYi0RJO_fDZGjL9xTe5JGJahAAuKJGFXzHFrp73C9YBsOXpm4Afjv1SMhLI8l0iYJWzsf_DbDM',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

r = requests.post(url, json=payload, headers=headers)
# Load the response into a pandas dataframe
df = pd.DataFrame(r.json()['data'])
df_headers = ['ID', 'Company', 'Product', 'HTSUSCode',
                'PublicStatus', 'WindowClose', 'PublishDate']
df.columns = df_headers

ID_headers = {
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

element_xpath = {
    "Product Inforamtion": {
        "Submission Date": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[1]/p/span",
        "Public Status": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[2]/p/span",
        "Product Type": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[3]/div[1]/input",
        "Identify the class of product for which the Exclusion is sought": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[3]/div[2]/input",
        "10-Digit Harmonized Tariff Schedule Code of the United States (HTSUS) for the single product covered by this request": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[4]/div[2]/input",
        "If this is a renewal of a previously granted exclusion request, please provide the ID number of the previously granted exclusion request": "/html/body/div[2]/div/div/form/div/div[1]/div[1]/div[5]/div[2]/input"
    },
    "Requesting Organization Information": {
        "Full Organization Legal Name": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[1]/div/div/input",
        "Street Address": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[2]/div[1]/div/input",
        "City": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[2]/div[2]/div/input",
        "State": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[1]/div/input",
        "Zip Code": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[2]/div/input",
        "Headquarters Country": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[3]/div/input",
        "Point of Contact Name": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[4]/div/input",
        "Phone Number": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[5]/div/input",
        "Email Address": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[6]/div/input",
        "Website Address": "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[3]/div[7]/div/input"
    },
    "Parent Company of Requesting Organization": {
        "Full Organization Legal Name": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[1]/div/div/input",
        "Street Address": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[2]/div[1]/div/input",
        "City": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/input",
        "Headquarters Country": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[3]/div[1]/div/input",
        "State/Province": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[3]/div[2]/div/input",
        "Zip Code": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[3]/div[3]/div/input",
        "Website Address": "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div[3]/div[4]/div/input"
    },
    "Importer of Record for Organization Requesting an Exclusion": {
        "Full Organization Legal Name": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[1]/div/div/input",
        "Street Address": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[2]/div[1]/div/input",
        "City": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[2]/div[2]/div/input",
        "State": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[1]/div/input",
        "Zip Code": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[2]/div/input",
        "Headquarters Country": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[3]/div/input",
        "Point of Contact Name": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[4]/div/input",
        "Phone Number": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[5]/div/input",
        "Email Address": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[6]/div/input",
        "Website Address": "/html/body/div[2]/div/div/form/div/div[1]/div[5]/div[3]/div[7]/div/input"
    },
    "Requester's Authorized Representative/Agent (if applicable)": {
        "Requester Point of Contact Name": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[1]/div/input",
        "Point-of-Contact Organization": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[2]/div/input",
        "Country Location": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[3]/div/input",
        "Phone Number": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[4]/div/input",
        "Email Address": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[5]/div/input",
        "Website Address": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[6]/div/input",
        "Other Information": "/html/body/div[2]/div/div/form/div/div[2]/div[1]/div/div[7]/div/textarea"
    },
    "Exclusion Request Details": {
        "Does the parent organization hold ownership in (partially or completely), or is it otherwise engaged as a: Manufacturer; Distributor; Exporter or, Importer?": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/input",
        "Identify the activity": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/input",
        "Identify the organization": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/input",
        "Identify the country where the organization is headquartered": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/input",
        "Comments": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[3]/textarea",
        "Identify the primary type of activity of the Exclusion Requester": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[4]/div[1]/div/input",
        "Comments2": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/textarea",
        "Total Requested Annual Exclusion Quantity in Kilograms (1 metric ton = 1,000 kilograms)": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[5]/div[2]/div/input",
        "Units": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div[5]/div[2]/div/div/span",
        "Average annual consumption for years 2015-2017 of the product that is subject of this Exclusion Request (Kilograms)": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[2]/div/div[2]/div/input",
        "Units2": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span",
        "Explain why your organization requires an Exclusion": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[3]/div[1]/div/input",
        "Please provide comments": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[3]/div[2]/div/textarea",
        "Identify the percentage of total product covered under this Exclusion Request not available from manufacturers in the United States": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[4]/div[2]/div/input",
        "Estimate the number of days required to take delivery of the product covered by this Exclusion Request, from the time the purchase order is issued by your organization": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[5]/div[2]/div/input",
        "Estimate the number of days required to manufacture the product covered by this Exclusion Request, from the time a binding purchase order is executed": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[6]/div[2]/div/input",
        "Estimate the number of days required to ship the product covered under this Exclusion Request, from the foreign port of departure to the Exclusion Requester's loading dock": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[7]/div[2]/div/input",
        "Estimate the number of distinct shipments from the foreign port(s) of departure that will be needed for transporting to the United States the product subject to this Exclusion Request": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[8]/div[2]/div/input",
        "Identify the U.S. Destination Port(s) of Entry through which the product subject to this Exclusion Request would be transported": "class|portstable/table",
        "Is the organization making this Exclusion Request doing so on behalf of a non-U.S. producer that does not manufacture products in the United States?": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[10]/div[2]/input",
        "Identify the non-U.S. producer": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[11]/div[1]/input",
        "Identify the country where the organization is headquartered2": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[11]/div[2]/input",
        "Comments3": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[11]/div[3]/textarea"
    }, 
    "Exclusion Request Product Information": {
        "For this single Exclusion Request, provide a full, complete description of the product in the space provided below.See explanation below. The product for which an Exclusion is being requested is defined as follows:": "/html/body/div[2]/div/div/form/div/div[3]/div[1]/div/div[1]/textarea",
        "Comments": "/html/body/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/textarea",
        "Identify the standards organizations that have set specifications for the product type that is the subject of this Exclusion Request, and provide the reference designation(s) for the identified standards organization(s), (e.g., ASTM A108-13):": "class|productstandardstable/table",
        "Identify the classification and properties of the product covered under this Exclusion Request. Other classification or properties may be described in the textboxes below. (Select all that apply)": "xpath|/html/body/div[2]/div/div/form/div/div[3]/div[2]/div[2]/div[2]/table[1]/table"
    }
}

# Iterate over records
for index, row in df.iterrows():

    # Headless Chrome driver
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/Users/ericmckevitt/Documents/chromedriver', options=options)

    id = row['ID']
    print(f"\n--------------------\nProcessing {id}:\n--------------------\n")

    if DEBUG:
        id = 325609

    # For each id, make a request to the detail page
    url = f'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/{id}'

    driver.get(url)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'lxml')

    dom = etree.HTML(str(soup))

    # For each section, grab all the elements
    for section in element_xpath:
        # For each element, get the value and print it
        print(f"\n{section}:\n")
        for element in element_xpath[section]:
            xpath = element_xpath[section][element]

            # If the element ends in input, then it is an input field
            if xpath.endswith('input'):
                print(f"{element}:", dom.xpath(f'{xpath}')[0].get('value'))

            elif xpath.endswith('textarea'):
                print(f"{element}:", dom.xpath(f'{xpath}')[0].text)

            elif xpath.endswith('table'):
                result = ""
                prefix = xpath.split('|')[0]
                identifier = xpath.split('|')[1]

                # remove everything after the last / in identifier
                identifier = identifier[:identifier.rfind('/')]
                
                # if the prefix contains "class" 
                if prefix == "class":
                    table = soup.find('table', {'class': identifier})
                    result = cd.cleanDataByClassName(table, identifier)
                elif prefix == 'xpath':
                    table = soup.find('table', {'xpath': prefix})
                    table = dom.xpath(f'{identifier}')[0]
                    result = cd.cleanDataByXpath(table, identifier)
                print(f"{element}:", result)

            else:
                print(f"{element}:", dom.xpath(f'{xpath}')[0].text)


    if DEBUG:
        print("\n")
        break
