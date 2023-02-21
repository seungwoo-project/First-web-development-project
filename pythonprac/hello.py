from pymongo import MongoClient
import certifi 

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.d4m39ds.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.dbsparta

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(3)

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a=tr.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = tr.select_one('td.ac>img')['alt']
        star=tr.select_one('td.point').text
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star
        }
        db.movies.insert_one(doc)
