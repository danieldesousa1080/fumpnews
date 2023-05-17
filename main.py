from requests import get
from bs4 import BeautifulSoup as bs
import json


class Fumpnews():
    def __init__(self, page_number=1):
        self.base_url = "https://www.fump.ufmg.br/"
        self.url = self.base_url + f"noticias.aspx?pag={page_number}"
        self.response = get(self.url)
        self.soup = bs(self.response.text, "html.parser")

        self.news_container = self.soup.find(id="contentPlaceHolder_colLeft")
        self.news_list = self.news_container.find_all("tr")
        self.last_page = int(self.news_container.find(
            "ul", class_="inline").find_all("li")[1].text.split("/")[1])

    def get_news(self, save=False, output="dumps.json"):
        newslist = []
        for news in self.news_list:
            date = news.find("div").text.strip().replace(".", "/")
            text = news.find("a").text.strip()
            link = news.find("a").get("href").replace("¬", "&not")
            link = self.base_url + link
            newslist.append(
                {"date": date,
                 "text": text,
                 "link": link}
            )
        if save:
            newsdict = {}
            for i in range(len(newslist)):
                newsdict[i] = newslist[i]

            with open(output, "w") as file:
                json_obj = json.dumps(newsdict)
                file.write(json_obj)

            print(file)

        return newslist


url = "https://www.fump.ufmg.br/noticias.aspx"
response = get(url)
soup = bs(response.text, "html.parser")
last_page = int(soup.find(id="contentPlaceHolder_colLeft").find(
    "ul", class_="inline").find_all("li")[1].text.split("/")[1])

for i in range(5, 0, -1):
    print("Página", i)
    Fumpnews(i).get_news(True)
