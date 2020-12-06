#!/use/bin/env python3

import requests
import sys
from pathlib import Path

url = "https://movie.douban.com/top250"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'

header = {'user-agent': user_agent}
try:    
    response = requests.get(url, headers=header)
except requests.exceptions.ConnectTimeout as e:
    print('requests库超时')
    sys.exit(1)


# 存储html文件路径及文件
file_path = Path(__file__).resolve().parent  # 获取脚本所在位置的路径
html_path = file_path.joinpath('html')      # 设置html存储文件所在路径
if not html_path.is_dir():                      
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')     # 设置html文件路径


try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print('文件无法打开')
except IOError as e:
    print('文件读写错误')
except Exception as e:
    print(f'其它错误 {e}')










