import re

import requests


def request_dangdang(url):
    response = requests.get(url)
    html = response.text
    return html


def parse_response(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class'
        '="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span'
        '>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '图片': item[1],
            '书名': item[2],
            '推荐指数': item[3],
            '作者': item[4],
            '五星评分次数': item[5],
            '价格': item[6]
        }


def write_to_file(date):
    try:
        print('写入数据ing----', date)
        with open('test/a.txt', 'a+', encoding='utf-8') as f:
            f.write(str(date) + '\n')
            f.close()
        print('写入数据成功')
    except IOError:
        print("写入{}异常".format(date))
    pass


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dangdang(url)
    y = parse_response(html)
    for x in y:
        write_to_file(x)
        pass


if __name__ == '__main__':
    for i in range(1, 2):
        main(i)
