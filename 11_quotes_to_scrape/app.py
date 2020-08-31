from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError


try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input('Enter your tag: ')

    firefox = webdriver.Firefox(executable_path='./geckodriver')
    firefox.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(firefox)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print('An unknown error occured. Please, try again.')
