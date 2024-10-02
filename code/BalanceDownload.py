import requests
import json

# DOWNLOAD BALANCE SHEET FROM ALPHA VANTAGE
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=I9YH4A8QRVGNJ88X'
r = requests.get(url)

# EXTRACT JSON AND APPLY PRETTY PRINT
data = r.content
parsed = json.loads(data)
pretty_json = json.dumps(parsed, indent=4)
# print(pretty_json)

# data = r.json()  # this one return a dict for easy traversal
# print(data)

# SAVE INTO A FILE
with open('raw_downloaded_data/ibm_balance.txt', 'w') as file:
    file.write(pretty_json)