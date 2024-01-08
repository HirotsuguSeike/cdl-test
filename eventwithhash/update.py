import requests
import json
import sys

def publish(dataprovider, filepath, filetype, datatagkey, datatagval, previouseventid):
    url = "http://172.28.16.71:3000/v2/eventwithhash"
    headers = {
        "Content-type": "multipart/form-data",
        "Authorization": "test"
    }
    # 来歴登録されるイベントに関するJSON
    jsondata = {
        "cdldatamodelversion":"2.0",
        "cdleventtype": "Update",
        "dataprovider": dataprovider,
        "cdlpreviousevents": [ previouseventid ],  
        "cdldatatags": [{datatagkey: datatagval}]
    }
    # 送信するファイルオブジェクト
    fileobj =  open(filepath, "rb")
    upfileTuple =  (filepath.split('/')[-1], fileobj, filetype)
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
    if len(sys.argv) != 8 or sys.argv[1] == "help" or sys.argv[1] != "Update":
        print("How to use: ")
        print("  python3 eventwithhash.py Update [dataprovider] [filepath] [filetype] [datatagkey] [datatagval] [previouseventid]")
        print("  Remarks: filetype examples ('text/plain', 'image/jpeg', 'image/png')")
    else: 
        publish(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    

main()
