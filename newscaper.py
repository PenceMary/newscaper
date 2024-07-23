import requests
from bs4 import BeautifulSoup

def fetch_news(url, headline_tag, headline_class=None, base_url=''):
    print(f"Fetching news from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    news_headlines = []

    if headline_class:
        items = soup.find_all(headline_tag, class_=headline_class)
    else:
        items = soup.find_all(headline_tag)

    print(f"Found {len(items)} items on {url}")  # 调试信息

    for item in items:
        title = item.get_text().strip()
        link_tag = item.find('a')
        if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
            full_link = link if link.startswith('http') else f"{base_url}{link}"
            news_headlines.append((title, full_link))

    return news_headlines

def get_cnn_news():
    return fetch_news('https://edition.cnn.com/world', 'span', 'cd__headline-text', 'https://edition.cnn.com')

def get_xinhua_news():
    return fetch_news('http://www.xinhuanet.com/english/world/index.htm', 'h3', base_url='http://www.xinhuanet.com')

def get_bbc_news():
    return fetch_news('https://www.bbc.com/news', 'h3', base_url='https://www.bbc.com')

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