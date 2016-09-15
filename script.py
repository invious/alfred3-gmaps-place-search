import requests

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

querystring = {"query": "Van Dyke Technology Group",
               "key": "AIzaSyC0r4UxnX_COKvG10vK_NBjon-4CNKJeCI"}

headers = {
    'cache-control': "no-cache",
}

response = requests.request("GET", url, headers=headers, params=querystring)

print response.json()['results'][0]['formatted_address']
