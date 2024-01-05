import requests

def main(): 
    url = "http://172.28.16.71:3000/v2/searchevents"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "selector": {
            "dataprovider": "AAA-BBB"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print("Status code:", response.status_code)
    print("Response body:", response.text)

main()
