import requests
import pymysql
import sys
from lxml import etree
from time import sleep
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from movie_comment_storge import Movie, Comment


dburl = 'mysql+pymysql://devops:qwe123456@node1:3306/db1?charset=utf8mb4'
engine = create_engine(dburl, echo=True, encoding='utf-8')
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 清除历史数据
q = session.query(Movie)
q.delete()
c = session.query(Comment)
c.delete()
session.commit()



ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {
    'user-agent': ua
}

url = 'https://movie.douban.com/top250'

num = 10

def get_movie_comment(url):
    try:
        res = requests.get(url, headers = header)
    except Exception as e:
        print(f'get {url} err {e}')
        sys.exit(1)

    selector = etree.HTML(res.text)
    movie_name = selector.xpath('//div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
    movie_url = selector.xpath('//div[@class="info"]/div[@class="hd"]/a/@href')

    movie_urls = zip(movie_name[:num], movie_url[:num])

    for name, url in movie_urls:
        movie = Movie(name=name)  
        session.add(movie)
        # session.commit()
        que = session.query(Movie).filter(Movie.name==name).first()
        print(type(que.id))

        res = requests.get(url, headers = header)
        selector = etree.HTML(res.text)
        comment_url = selector.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/@href')
        # https://movie.douban.com/subject/1292052/comments?status=P
        # https://movie.douban.com/subject/1292052/comments?start=20&limit=20&status=P&sort=new_score
        comment_url = f"{comment_url[0]}&start=0&limit=20&sort=new_score"

        res = requests.get(comment_url, headers = header)
        selector = etree.HTML(res.text)
        n_stars = selector.xpath('//div[@class="comment"]/h3/span[2]/span[2]/@title')
        comments = selector.xpath('//div[@class="comment"]/p/span/text()')
        comment_infos = zip(n_stars, comments)

        for star, comm in comment_infos:
            # print(f'{star}: {comm}' )
            if star == '力荐':
                star = 5
            elif star == '推荐':
                star = 4
            elif star == '还行':
                star = 3
            elif star == '较差':
                star = 2
            else:
                star = 1

            c = Comment(movie_id=que.id, star=star, comm=comm)
            print(c)
            session.add(c)
            session.commit()
        
        sleep(5)
    
    # 1星：很差
    # 2星：较差
    # 3星：还行
    # 4星：推荐
    # 5星：力荐



    

get_movie_comment(url)
# for name, info in res:
#     print(name, end='\n\n')
#     print(type(info))
#     for comm in info:
#         print(f'{comm[0]}:\t{comm[1]}')




    
