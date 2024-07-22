import requests
from bs4 import BeautifulSoup

def get_cnn_news():
        url = 'https://edition.cnn.com/world'
            response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')

                    news_headlines = []
                        for item in soup.find_all('h3', class_='cd__headline'):
                                    title = item.get_text()
                                            link = item.find('a')['href']
                                                    full_link = f"https://edition.cnn.com{link}"
                                                            news_headlines.append((title, full_link))

                                                                return news_headlines

                                                            def get_xinhua_news():
                                                                    url = 'http://www.xinhuanet.com/english/world/index.htm'
                                                                        response = requests.get(url)
                                                                            soup = BeautifulSoup(response.content, 'html.parser')

                                                                                news_headlines = []
                                                                                    for item in soup.find_all('h3')
                                                                                                title = item.get_text()
                                                                                                        link = item.find('a')['href']
                                                                                                                full_link = link if link.startswith('http') else f"http://www.xinhuanet.com{link}"
                                                                                                                        news_headlines.append((title, full_link))

                                                                                                                            return news_headlines

                                                                                                                        def main():
                                                                                                                                cnn_news = get_cnn_news()
                                                                                                                                    xinhua_news = get_xinhua_news()

                                                                                                                                        print("CNN Latest News:")
                                                                                                                                            for title, link in cnn_news:
                                                                                                                                                        print(f"{title}\nLink: {link}\n")

                                                                                                                                                            print("Xinhua Latest News:")
                                                                                                                                                                for title, link in xinhua_news:
                                                                                                                                                                            print(f"{title}\nLink: {link}\n")

                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                    main()
