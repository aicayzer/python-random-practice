from requests import get
from bs4 import BeautifulSoup
from csv import writer

scraped_info = []

def scrape_page(base_url):
    parsed_html = get_html_for_url(base_url)
    articles = get_all_articles(parsed_html)

    # Scrape articles on home page
    scrape_articles(articles)

    # Scrape articles in additional pages
    last_page_element = parsed_html.find("span", class_="last")
    last_page_number = int(last_page_element.find("a")["href"].split("=")[1])

    for page_number in range(2, last_page_number + 1):
        parsed_html = get_html_for_url(f"{base_url}?page={page_number}")
        articles = get_all_articles(parsed_html)

        scrape_articles(articles)

def get_html_for_url(url):
    response = get(url)
    return BeautifulSoup(response.text, "html.parser")

def get_all_articles(bs_html):
    return bs_html.find_all("article")

def scrape_articles(articles):
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        link = a_tag["href"]
        date = article.find("time")["datetime"]

        scraped_info.append({"title":title, "link":link, "date":date})

def write_results_to_file():
    with open("blog_data.csv", "w") as f_result:
        f_writer = writer(f_result)
        f_writer.writerow(["Title", "Link", "Date"])

        for si in scraped_info:
            f_writer.writerow([si["title"], si["link"], si["date"]])

scrape_page("https://www.rithmschool.com/blog")
write_results_to_file()





# import requests
# from bs4 import BeautifulSoup
# import csv
#
# response = requests.get("https://www.rithmschool.com/blog")
# soup = BeautifulSoup(response.text, "html.parser")
# articles = soup.find_all("article")
#
# with open("blog_data.csv", "w") as csv_writer:
#     csvwriter = csv.writer(csv_writer)
#     csvwriter.writerow(["title", "link", "date"])
#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag["href"]
#         date = article.find("time")["datetime"]
#         csvwriter.writerow([title, url, date])
#
#
# # with open ("blog_data.csv") as csvfile:
# #     reader = csv.reader(csvfile)
# #     print(csvfile.read())
