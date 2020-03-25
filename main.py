import requests
import json
from urllib.parse import urlparse
import os.path

ua = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36'
headers = {'User-Agent' : ua}
response = requests.get("https://qiita.com/api/v2/users/kwmt@github/items?page=1&per_page=20", headers=headers).text
results = json.loads(response)

content_dir = './content'
# create content dir
os.makedirs(content_dir, exist_ok=True)

def writ_file(path, content):
    with open(path, mode='w') as f:
        f.write(content)

for result in results:
    url = result['url']
    title = result['title']
    # split_path = os.path.split(urlparse(url).path)
    # file_path = content_dir + '/' + split_path[1] + '.md'
    file_path = content_dir + '/' + title + '.md'
    markdown_url = url + '.md'
    content = requests.get(markdown_url, headers=headers).text
    writ_file(file_path, content)


