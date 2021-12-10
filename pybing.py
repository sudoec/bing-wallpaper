#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import datetime
import time


def main():
    # 请求主页面
    url = "https://cn.bing.com"
    rs = requests.get(url=url)

    # 对网页解析
    html = etree.HTML(rs.content)
    imgUrl = 'https://cn.bing.com' + html.xpath('//*[@id="preloadBg"]/@href')[0]

    # 获取图片内容
    imgRs = requests.get(url=imgUrl)

    time = datetime.datetime.now()
    str_time = datetime.datetime.strftime(time, "%Y-%m-%d")
    print(time)
    path = "./{}.jpg".format(str_time)
    with open(path, "wb") as f:
        f.write(imgRs.content)


if __name__ == '__main__':
        main()