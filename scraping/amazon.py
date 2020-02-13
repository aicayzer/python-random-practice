from requests import get
from bs4 import BeautifulSoup
import csv


# def newcsv():
#     with open("quotes.csv", "w") as file:
#         csvwriter = csv.writer(file)


# def grabber(url):
#     with open("quotes.csv", "a") as file:
#         csvwriter = csv.writer(file)
#         response = get(url).text
#         soup = BeautifulSoup(response, "html.parser")
#         quotes = soup.find_all(class_="quote")
#         for q in quotes:
#             quote = q.find(class_="text").get_text()
#             by = q.find(class_="author").get_text()
#             csvwriter.writerow([quote, by])
#
#
# def pages(url):
#     response = get(url)
#     next_request = url
#     i = 10
#     j = 10
#     while True:
#         try:
#             print(f"LOADING.... {i}% of the way there")
#             grabber(next_request)
#             soup = BeautifulSoup(response.text, "html.parser")
#             next_button = soup.find(class_="next")
#             next_page = next_button.find("a")["href"]
#             next_request = (f"{url}{next_page}")
#             response = get(next_request)
#             i += j
#         except BaseException:
#             break


def scraper():
    response = get("http://www.amazon.co.uk").text
    soup  = BeautifulSoup(response, "html.parser")
    images = (soup.find_all(class_="product-image"))
    for image in images:
        print(image).get_text()

    print(images)





scraper()
