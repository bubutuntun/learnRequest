import time

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
wait = WebDriverWait(driver, 10)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('蔡徐坤篮球', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕数')
sheet.write(0, 5, '发布时间')

n = 1


def save_to_excel(soup):
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')

    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text

        print('爬取：' + item_title)

        global n

        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biubiu)
        sheet.write(n, 5, item_date)

        n = n + 1
    pass


# 获取网页源代码解析
def get_source():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)
    pass


def search():
    driver.get("https://www.bilibili.com/")
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a"))).click()

    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-search-keyword")))
    time.sleep(2)
    # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bilifont bili-icon_dingdao_sousuo nav-search-submit")))

    input.send_keys('蔡徐坤 篮球')
    driver.find_element(By.CSS_SELECTOR, ".bilifont bili-icon_dingdao_sousuo nav-search-submit").click()
    # submit.click()
    # 跳转到新的窗口
    print('跳转到新的窗口')
    # 获取所有窗口句柄
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[1])
    get_source()


def main():
    search()


if __name__ == '__main__':
    main()
    book.save(u'蔡徐坤篮球.xlsx')
