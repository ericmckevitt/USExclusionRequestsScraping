from lxml import etree
import requests
from bs4 import BeautifulSoup

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

def portsTable(table):
    print("\nPorts Table:")

    # Use bs4 to parse the table
    soup = BeautifulSoup(etree.tostring(table), 'html.parser')
    table = soup.find('table')
    print(f"soup table: {table}")

    # Get tr elements
    trs = table.children
    print(f"trs: {list(trs)}")

    return "\nHITHERE"

def main():
    id = 325609
    # For each id, make a request to the detail page
    url = f'https://232app.azurewebsites.net/Forms/ExclusionRequestItem/{id}'
    r = requests.get(url)

    # Save the HTML response and parse the DOM
    soup = BeautifulSoup(r.text, 'html.parser')
    dom = etree.HTML(str(soup))

    xpath = "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[9]/div[2]/table"
    table = dom.xpath(xpath)[0]

    # Get the table's parent
    parent = table.getparent()
    print(f"parent: {parent}")
    print(f"parent class: {parent.attrib['class']}")

    # Get the table's children
    children = table.getchildren()
    # print(f"children: {children}")

    tables = soup.find_all('table')
    for table in tables:
        class_name = table.get('class')
        print(f"class_name: {class_name}")
        # if has children
        if table.findChildren():
            children = table.findChildren()
            tr_list = [ tr for tr in children if tr.name == 'tr' ]
            print(f"\tchildren: {tr_list}")
        else:
            print(f"\tNo children")
        print('\n')

    # print(f"\n\nTable before call: {table}\n\n")
    # portsTable(table)

    # print(r.text)

    # table = soup.find('table', class="portstable")

    # Find table by class name
    # table = soup.find('table', class_="table table-bordered bg-white tblsourcecountries")
    # print(f"\n\nTable before call: {table}\n\n")


    # Find table with class name = "tblsourcecountries"
    # table = soup.find('table', class_="tblsourcecountries")
    # tr_list = table.findChildren('tr')
    # print(f"tr_list: {tr_list}")

    print("----------------------------------------------")

    class_name = "portstable"
    table = soup.find('table', class_=class_name)
    print(f"table: {table}")

    print(r.text)

if __name__ == "__main__":
    main()