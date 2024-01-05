import requests
import sys
    

def main():
    url = "http://172.28.16.71:3000/v2/lineage/77aab51b-7c5b-446e-bc88-282cc4832ca6"
    headers = {
        "Authorization": "test"
    }
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print("Response body:", response.text)

main()
