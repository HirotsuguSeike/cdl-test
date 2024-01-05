import requests
import json
import sys

def create(dataprovider, filepath, filetype, datatagkey, datatagval):
    url = "http://172.28.16.71:3000/v2/eventwithhash"
    headers = {
        "Content-type": "multipart/form-data",
        "Authorization": "test"
    }
    # 来歴登録されるイベントに関するJSON
    jsondata = {
        "cdldatamodelversion":"2.0",
        "cdleventtype": "Create",
        "dataprovider": dataprovider, 
        "cdldatatags": [{datatagkey: datatagval}]
    }
    # 送信するファイルオブジェクト
    fileobj =  open(filepath, "rb")
    upfileTuple =  (filepath.split('/')[-1], fileobj, 'text/plain')
    # マルチパートデータを構築
    files = {
        'request': ('req.json', json.dumps(jsondata), 'application/json'), 
        'upfile': upfileTuple
    }
    # リクエストを送信
    try:
        response = requests.post(url, files=files)
        print("Status code:", response.status_code)
        print("Response body:", response.text)
    except Exception as e:
        print(e)
    # ファイルオブジェクトをクローズ
    fileobj.close() 
    
def main():
    if len(sys.argv) != 7 or sys.argv[1] == "help" or sys.argv[1] != "Create":
        print("How to use: ")
        print("  python3 eventwithhash.py Create [dataprovider] [filepath] [filetype] [datatagkey] [datatagval]")
        print("  Remarks: filetype examples ('text/plain', 'image/jpeg', 'image/png')")
    else: 
        create(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    

main()
