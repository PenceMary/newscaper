from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fetch_news_with_selenium(url, headline_tag, headline_class=None, base_url=''):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    news_headlines = []
    if headline_class:
        items = soup.find_all(headline_tag, class_=headline_class)
    else:
        items = soup.find_all(headline_tag)

    for item in items:
        title = item.get_text().strip()
        link_tag = item.find('a')
        if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
            full_link = link if link.startswith('http') else f"{base_url}{link}"
            news_headlines.append((title, full_link))

    return news_headlines

def get_cnn_news():
    return fetch_news_with_selenium('https://edition.cnn.com/world', 'h3', 'cd__headline', 'https://edition.cnn.com')

def get_xinhua_news():
    return fetch_news_with_selenium('http://www.xinhuanet.com/english/world/index.htm', 'h3', base_url='http://www.xinhuanet.com')

def get_bbc_news():
    return fetch_news_with_selenium('https://www.bbc.com/news', 'h3', base_url='https://www.bbc.com')

def main():
    news_sources = {
        "CNN": get_cnn_news(),
        "Xinhua": get_xinhua_news(),
        "BBC": get_bbc_news()
    }

    for source, news in news_sources.items():
        print(f"{source} Latest News:")
        if news:
            for title, link in news:
                print(f"{title}\nLink: {link}\n")
        else:
            print("No news found")
        print("-" * 50)

if __name__ == "__main__":
    main()