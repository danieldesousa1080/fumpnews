from requests import get, Session
from bs4 import BeautifulSoup as bs
import database_config as dc


class Fumpnews():
    def __init__(self, page_number=1):
        self.session = Session()
        self.base_url = "https://www.fump.ufmg.br/"
        self.url = self.base_url + f"noticias.aspx?pag={page_number}"
        self.response = self.session.get(self.url)
        self.soup = bs(self.response.text, "html.parser")

        self.news_container = self.soup.find(id="contentPlaceHolder_colLeft")
        self.news_list = self.news_container.find_all("tr")
        self.last_page = int(self.news_container.find(
            "ul", class_="inline").find_all("li")[1].text.split("/")[1])

    def get_news(self):

        for news in self.news_list[::-1]:
            date = news.find("div").text.strip().replace(".", "/")
            title = news.find("a").text.strip()
            link = news.find("a").get("href").replace("¬", "&not")
            link = self.base_url + link

            news_html = self.session.get(link).text
            news_soup = bs(news_html,"html.parser")
            news_text = str(news_soup.find(id="contentPlaceHolder_defaultNewsContainer"))

            dc.add_news(date, title, news_text, link)


url = "https://www.fump.ufmg.br/noticias.aspx"
response = get(url)
soup = bs(response.text, "html.parser")
last_page = int(soup.find(id="contentPlaceHolder_colLeft").find(
    "ul", class_="inline").find_all("li")[1].text.split("/")[1])


def get_last_news_from_page(page):
    for i in range(page, 0, -1):
        print("Página", i)
        Fumpnews(i).get_news()

if __name__ == "__main__":
    get_last_news_from_page(last_page)