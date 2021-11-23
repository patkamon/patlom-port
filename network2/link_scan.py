from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import sys
from typing import List
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_links(url: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    link = []
    driver.get(url)
    elements = driver.find_elements_by_tag_name('a')
    for e in elements:
        href = e.get_attribute('href')
        #not include path with # or ?
        try:
            href = href.split('?')[0]
            href = href.split('#')[0]

            if href not in link:
                link.append(href)
        except:
            pass
    return link

def is_valid_url(url: str):
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request, context=ctx)
        return True
    except:
        return False

def invalid_url(urllist: List[str]) -> List[str]:
    invalid_list = []
    for url in urllist:
        if is_valid_url(url) == False:
            invalid_list.append(url)
    return invalid_list

if __name__ == '__main__':
    if len(sys.argv) > 1:
        list = get_links(sys.argv[1])
        for link in list:
            print(link)
        print('#--------------#')
        print('Bad Links:')
        bad_list = invalid_url(list)
        for bad_link in bad_list:
            print(bad_link)
    else:
        print(f'Usage:  python3 {sys.argv[0]} url')
        print('Test all hyperlinks on the given url.')


