import requests
import sys
    

def main():
    url = "http://172.28.16.71:3000/v2/lineage/46c55b64-ac20-4d9c-b505-72416aac8be6"
    if len(sys.argv) == 2:
        url = f"http://172.28.16.71:3000/v2/lineage/{sys.argv[1]}"
    headers = {
        "Authorization": "test"
    }
    params = {"direction": "FORWARD", "depth": 2}
    response = requests.get(url, headers=headers, params=params)
    print("Status code:", response.status_code)
    print("Response body:", response.text)

main()
