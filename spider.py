# -*- coding: utf-8 -*-

import bs4
from bs4 import BeautifulSoup
import tomd
import requests
import time

class ArticleNode:
    depth = 0
    name = ''
    id=''
    url = ''
    articleHTML = ''
    articleMD = ''
    imgs = []
    children = []

    def __init__(self, depth=0, url='', name=''):
        self.depth = depth
        self.url = url
        self.name = name

    def toString(self):
        return "depth: " + str(self.depth) + "\nname: " + self.name + "\nid: " + self.id + "\nurl: " + self.url + "\n" + self.articleMD

    def parse(self):
        pass

rootPage = 'https://www.liaoxuefeng.com/wiki/1016959663602400'
    
def getUrlContent(url):
    """
    description: 获取指定url的内容\n
    param url: 链接地址\n
    return: 返回链接的页面内容，html文本。\n
        如果出错，返回None。
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def getIndex(url):
    content = getUrlContent(url)

    if content != None:
        soup = BeautifulSoup(content, 'lxml')
        indexTree = soup.find('ul', id='x-wiki-index').find('div')
        getNode(indexTree)

def getNode(contentSoup):
    node = ArticleNode()
    node.depth = contentSoup['depth']
    node.id = contentSoup['id']
    node.name = contentSoup.find('a', class_='x-wiki-index-item').text
    node.url = 'https://www.liaoxuefeng.com' + contentSoup.find('a', class_='x-wiki-index-item')['href']
    
    content = getUrlContent(node.url)
    if content != None:
        soup = BeautifulSoup(content, 'lxml')
        node.articleHTML = str(soup.find('div', class_="x-wiki-content x-main-content"))
        node.articleMD = tomd.convert(node.articleHTML)
    
    for item in contentSoup.find_all('div', depth=str(int(node.depth)+1)):
        node.children.append(getNode(item))
            
    print(node.toString())
    return node
    
getIndex(rootPage)
