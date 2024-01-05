import requests
import json
import sys

def received(dataprovider, datauser, previouseventid):
    url = "http://172.28.16.71:3000/v2/eventwithhash"
    headers = {
        "Content-type": "multipart/form-data",
        "Authorization": "test"
    }
    # 来歴登録されるイベントに関するJSON
    jsondata = {
        "cdldatamodelversion":"2.0",
        "cdleventtype": "Received",
        "dataprovider": dataprovider,
        "datauser": datauser, 
        "cdlpreviousevents": [ previouseventid ]
    }
    # マルチパートデータを構築
    files = {
        'request': ('req.json', json.dumps(jsondata), 'application/json')
    }
    # リクエストを送信
    try:
        response = requests.post(url, files=files)
        print("Status code:", response.status_code)
        print("Response body:", response.text)
    except Exception as e:
        print(e)
    
def main():
    if len(sys.argv) != 5 or sys.argv[1] == "help" or sys.argv[1] != "Received":
        print("How to use: ")
        print("  python3 eventwithhash.py Received [dataprovider] [datauser] [previouseventid]")
    else: 
        received(sys.argv[2], sys.argv[3], sys.argv[4])
    

main()
