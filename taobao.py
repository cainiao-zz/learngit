import requests
url = 'https://s.taobao.com/image'

headers = {
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryetxEa6adCeAHhUms",
    "origin": "https://www.taobao.com",
    "referer": "https://www.taobao.com/?sprefer=sypc00",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
with open('./1.jpeg','rb') as f:
    img_data = f.read()
files = {'file':('1.jpeg', img_data, 'image/jpeg')}
response = requests.post(url=url, headers=headers, files=files)
if response.status_code == 200:
    print(response.status_code)
    print(response.content.decode())
else:
    print(response.status_code)