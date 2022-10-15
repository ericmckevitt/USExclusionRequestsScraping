import requests
import pprint

num_records = 10

url = 'https://232app.azurewebsites.net/Index?handler=SummaryView'

payload = {"draw": 1, "columns": [{"data": 0, "name": "ID", "searchable": True, "orderable": True, "search": {"value": "", "regex": False}},
                                  {"data": 1, "name": "Company", "searchable": True, "orderable": True, "search": {
                                      "value": "", "regex": False}},
                                  {"data": 2, "name": "Product", "searchable": True, "orderable": True, "search": {
                                      "value": "", "regex": False}},
                                  {"data": 3, "name": "HTSUSCode", "searchable": True, "orderable": True, "search": {
                                      "value": "", "regex": False}},
                                  {"data": 4, "name": "PublicStatus",
                                  "searchable": True, "orderable": True, "search": {"value": "", "regex": False}},
                                  {"data": 5, "name": "WindowClose", "searchable": True,
                                      "orderable": True, "search": {"value": "", "regex": False}},
                                  {"data": 6, "name": "PublishDate", "searchable": True,
                                      "orderable": True, "search": {"value": "", "regex": False}},
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

pprint.pprint(r.json())

# Loop over the records and print the ID
for record in r.json()['data']:
    print(record[0])
