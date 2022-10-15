import requests
import pprint
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import cleanData as cd

DEBUG = True

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

# pprint.pprint(r.json())

# print the size of the response
print(f"\n{len(r.json()['data'])} records returned")

# Load the response into a pandas dataframe
df = pd.DataFrame(r.json()['data'])

df_headers = ['ID', 'Company', 'Product', 'HTSUSCode',
                'PublicStatus', 'WindowClose', 'PublishDate']

df.columns = df_headers

# print the dataframe
# print(df)

# Save the dataframe to a csv file
# df.to_csv('232app.csv', index=False)

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
        "Identify the U.S. Destination Port(s) of Entry through which the product subject to this Exclusion Request would be transported": "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[9]/div[2]/table"
    }
}


# Iterate over records
for index, row in df.iterrows():

    id = row['ID']
    print(f"\n--------------------\nProcessing {id}:\n--------------------\n")

    if DEBUG:
        id = 325609

    # For each id, make a request to the detail page
    url = f'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/{id}'
    r = requests.get(url, headers=ID_headers)

    # Save the HTML response and parse the DOM
    soup = BeautifulSoup(r.text, 'html.parser')
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
                if dom.xpath(f'{xpath}')[0].get('class') == 'portstable':
                    # Get the table
                    table = dom.xpath(f'{xpath}')[0]
                    print(type(table))
                    print(cd.portsTable(table))
                    


            else:
                print(f"{element}:", dom.xpath(f'{xpath}')[0].text)

    if DEBUG:
        print("\n")
        break
