
# import requests
# from bs4 import BeautifulSoup
# import random
#
# quotes_list = []
# page = 1
# while True:
#     response = requests.get(f"http://quotes.toscrape.com/page/{page}/")
#     soup = BeautifulSoup(response.text, "html.parser")
#     no_quotes = soup.body.contents[1].find_all(class_="col-md-8")[1].get_text()
#     if "No quotes found!" in no_quotes:
#         break
#     else:
#         quotes = soup.find_all(class_="quote")
#
#         for quote in quotes:
#             quotes_list.append([quote.find(itemprop="text").get_text(),
#                                 quote.find(itemprop="author").get_text(),
#                                 quote.find("a")["href"]])
#         page += 1
#
#
# def get_hint(random_quote, next_hint):
#     if next_hint == 0:
#         hint_response = requests.get(
#             f"http://quotes.toscrape.com{random_quote[2]}")
#         hint_soup = BeautifulSoup(hint_response.text, "html.parser")
#         born = hint_soup.find(class_="author-born-date").get_text()
#         born_location = hint_soup.find(
#             class_="author-born-location").get_text()
#         print(f"Here is a hint: The author was born {born}, {born_location}")
#     elif next_hint == 1:
#         print(
#             f"Here is a hint: The author's first name starts with {random_quote[1][0].upper()}")
#     elif next_hint == 2:
#         surname = (random_quote[1].split(" ")[1][0]).upper()
#         print(f"Here is a hint: The author's last name starts with {surname}")
#
#
# def play_again():
#     replay = input("Would you like to play again? (y/n) > ")
#     if replay.upper() == "y":
#         print("Great! Here we go again...\n")
#         game()
#     else:
#         print("OK. See you next time.")
#         exit()
#
#
# def game():
#     random_quote = random.choice(quotes_list)
#     guesses_left = 4
#     next_hint = 0
#     print(f"{random_quote[0]}")
#     guess = input(f"\nWho said this? Guesses remaining: {guesses_left}. > ")
#
#     while True:
#         if guess == random_quote[1]:
#             print("You guessed correctly! Congratulations!")
#             play_again()
#         else:
#             guesses_left -= 1
#             if guesses_left == 0:
#                 print(
#                     f"You are out of guesses! The author was {random_quote[1]}")
#                 play_again()
#             get_hint(random_quote, next_hint)
#             next_hint += 1
#             guess = input(
#                 f"\nWho said this? Guesses remaining: {guesses_left}. > ")
#
#
# game()



















from requests import get
from bs4 import BeautifulSoup
import csv


def newcsv():
    with open("quotes.csv", "w") as file:
        csvwriter = csv.writer(file)


def grabber(url):
    with open("quotes.csv", "a") as file:
        csvwriter = csv.writer(file)
        response = get(url).text
        soup = BeautifulSoup(response, "html.parser")
        quotes = soup.find_all(class_="quote")
        for q in quotes:
            quote = q.find(class_="text").get_text()
            by = q.find(class_="author").get_text()
            csvwriter.writerow([quote, by])


def pages(url):
    response = get(url)
    next_request = url
    i = 10
    j = 10
    while True:
        try:
            print(f"LOADING.... {i}% of the way there")
            grabber(next_request)
            soup = BeautifulSoup(response.text, "html.parser")
            next_button = soup.find(class_="next")
            next_page = next_button.find("a")["href"]
            next_request = (f"{url}{next_page}")
            response = get(next_request)
            i += j
        except BaseException:
            break


def game():
    newcsv()
    pages("http://quotes.toscrape.com")


game()
