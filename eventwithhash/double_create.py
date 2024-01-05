import requests
import json
import sys

def create():
    url = "http://172.28.16.71:3000/v2/eventwithhash"
    headers = {
        "Content-type": "multipart/form-data",
        "Authorization": "test"
    }
    # 来歴登録されるイベントに関するJSON
    jsondata = {
        "cdldatamodelversion":"2.0",
        "cdleventtype": "Create",
        "dataprovider": "AAA-BBB", 
        "cdldatatags": [{"cdluri": "https://seike.info/img/test.png"},
                        {"user-key": "user-val"} ]
    }
    # 送信するファイルオブジェクト
    fileobj1 =  open("./test.txt", "rb")
    upfileTuple1 =  ("test.txt", fileobj1, 'text/plain')
    fileobj2 =  open("./test.png", "rb")
    upfileTuple2 =  ("test.png", fileobj2, 'image/png')
    # マルチパートデータを構築
    files = {
        'request': ('req.json', json.dumps(jsondata), 'application/json'), 
        'upfile1': upfileTuple1,
        'upfile2': upfileTuple2, 
    }
    # リクエストを送信
    try:
        response = requests.post(url, files=files)
        print("Status code:", response.status_code)
        print("Response body:", response.text)
    except Exception as e:
        print(e)
    # ファイルオブジェクトをクローズ
    fileobj1.close()
    fileobj2.close() 
    
def main():
    create()
    

main()
