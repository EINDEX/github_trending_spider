#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : github_trending.py
@Created       : 2017/8/19
@Last Modified : 2017/8/19
"""
import requests
import datetime
import os
import asyncio
from bs4 import BeautifulSoup

uri = 'https://github.com'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,la;q=0.2',
}


def get_github_trending_by_lang(lang, times=0):
    url = f'https://github.com/trending/{ lang }'
    r = requests.get(url, headers=HEADERS)
    r.encoding = r.apparent_encoding
    if r.ok:
        res = []
        bs = BeautifulSoup(r.text, 'html.parser')
        repo_list = bs.find('ol', attrs={'class': 'repo-list'})
        for repo in repo_list.find_all('li'):
            title = repo.find('a')
            content = repo.find('p')
            if content:
                content = content.text.strip()
            res.append(f'- [{title.text.strip()}]([{uri}{title["href"]}]):{content}')
        else:
            return res
    else:

        return get_github_trending_by_lang(lang, times + 1)


def get_lang_list():
    with open('lang_list', 'r') as f:
        return [lang.strip() for lang in f.readlines()]


def write_file(data):
    now = datetime.datetime.now()
    langs = sorted(data.keys())

    if not os.path.exists(f'{now.year}'):
        os.mkdir(f'{now.year}')

    with open(f'{now.year}/{now.date()}.md', 'w', encoding='utf-8') as f:
        for lang in langs:
            f.write(f'### {lang}\n', )
            for repo in data[lang]:
                f.write(f'{repo}\n')


def github_commit():
    """
    git add .
    git commit
    git push
    """
    pass


def get_github_trending():
    data = {}
    lang_list = get_lang_list()
    for lang in lang_list:
        data[lang] = get_github_trending_by_lang(lang)

    write_file(data)
    github_commit()


def timer():
    get_github_trending()


if __name__ == '__main__':
    timer()
