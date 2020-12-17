from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":"C:/Users/sduer/Desktop/chromedriver"}

#   "/usr/local/bin/chromedriver"
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    # NOTE: we're using the chromedriver approach for another example,
    # but we could certainly use the requests library as well.
    browser = init_browser()
    listings = {}

    url = "https://portland.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["headline"] = soup.find("a", class_="result-title").get_text()
    listings["price"] = soup.find("span", class_="result-price").get_text()
    listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings
