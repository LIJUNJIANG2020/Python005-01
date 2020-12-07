import requests
from lxml import etree
# pip install lxml
from time import sleep
import sys
from pathlib import Path

# ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
url1 = "https://www.smzdm.com/fenlei/chaojiben/h1c4s0f0t0p1/b1687/#feed-main/"
header = {
    'user-agent': ua,
}

save = Path(__file__).parent.joinpath('comment')


def get_res(url):
    try:
        res = requests.get(url, headers=header)
    except Exception as e:
        print(f"页面获取失败- {e}")
        sys.exit(1)
    selector = etree.HTML(res.text)
    # print(f'1- {selector}')
    return selector


def get_urls(url):
    urls = {}
    selector = get_res(url)
    # print(f'2- {selector}')
    item_names = selector.xpath('//h5/a/text()')
    item_links = selector.xpath('//h5/a/@href')

    urls = dict(zip(item_names, item_links))

    return urls
     

if __name__ == "__main__":
    urls = get_urls(url1)
    with open(save, 'w') as f:
        for name, url in urls.items():
            selector = get_res(url)
            comment_list = selector.xpath('//li[@class="comment_list"]/div[2]/div[3]/div/p/span/text()')
            # comment = {'name': name, 'comment': comment_list}
            f.write(f'标题：{name}\n评论：\n')
            for i in comment_list:
                print(i)
                f.write(f'\t{i}\n')
            sleep(5)

