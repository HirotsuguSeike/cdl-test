import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    # ファイルをバイナリモードで開き、全データを読み取り
    with open(file_path, 'rb') as file:
        data = file.read()
        sha256.update(data)

    # ハッシュ値を16進数文字列として取得
    sha256_hash = sha256.hexdigest()

    return sha256_hash

def main():
    # ファイルのパスを指定してSHA-256ハッシュを計算
    print(f'test.txt の SHA-256 ハッシュ値: {calculate_sha256("test.txt")}')
    print(f'test.png の SHA-256 ハッシュ値: {calculate_sha256("test.png")}')

main()
