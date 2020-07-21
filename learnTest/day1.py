import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
    "Host": 'movie.douban.com'}
r = requests.get('https://movie.douban.com/top250', headers=head)
print(r.text.encode('utf-8'))
print(r.status_code)
