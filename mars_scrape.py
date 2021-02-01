import pandas as pd
from pprint import pprint
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/sduer/Desktop/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # create surf_data dict that we can insert into mongo
    mars_dict = {
        'news_title': " ",
        'news_p': " ",
        'feature_img': " ",
        'mars_table': " ",
        'cerberus_title': " " , 
        'cerberus_img': " ",
        'major_title': " " , 
        'major_img': " ",
        'schiaparelli_title': " " , 
        'schiaparelli_img': " ",
        'major_title': " " , 
        'major_img': " " 
    }

    # 1) visit URL to scrape Mars news-title and news-paragraph
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)
    time.sleep(2)
    html = browser.html

    # create a soup object from the html
    soup1=BeautifulSoup(browser.html, 'html.parser')
    element = soup1.find('li', class_='slide')
    mars_dict['news_title'] = element.find('div', class_='content_title').find('a').text
    mars_dict['news_p'] = element.find('div', class_='rollover_description_inner').text

    # 2) visit URL to scrape feature-image
    feature_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(feature_img_url)
    time.sleep(4)
    html = browser.html

    # create a soup object from the html
    soup2=BeautifulSoup(browser.html, 'html.parser')
    feature_img = soup2.find('article', class_='carousel_item').find('a', class_="button fancybox")['data-fancybox-href']
    mars_dict['feature_img'] = f"{feature_img_url}{feature_img}"
    

    # 3) visit URL to scrape Mars table-data
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)
    time.sleep(3)
    html = browser.html

    # create a soup object from the html
    soup3=BeautifulSoup(browser.html, 'html.parser')
    mars_fact_table_extract = soup3.find('table', class_='tablepress tablepress-id-p-mars')
    mars_fact_table_extract = pd.read_html(html)
    mars_fact_table_df = mars_fact_table_extract[0]
    mars_fact_table_df.columns = ['Description', 'Value']
    mars_dict['mars_table'] = mars_fact_table_df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None, table_id=None)

    # 4.1) visit URL to scrape Mars Hemisphere Image-Cerberus
    hemisphere_image_urls = {}
    mars_cerberus_hemisphere_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(mars_cerberus_hemisphere_url)
    time.sleep(3)
    html = browser.html

    # create a soup object from the html
    soup4=BeautifulSoup(browser.html, 'html.parser')
    mars_dict['cerberus_title'] = soup4.find('h2', class_='title').text
    mars_dict['cerberus_img'] = soup4.find('div', class_='downloads').find('a')["href"]

    # 4.2) visit URL to scrape Mars Hemisphere Image-Schiaparelli
    mars_schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(mars_schiaparelli_url)
    time.sleep(3)
    html = browser.html

    # create a soup object from the html
    soup5=BeautifulSoup(browser.html, 'html.parser')
    mars_dict['schiaparelli_title'] = soup5.find('h2', class_='title').text
    mars_dict['schiaparelli_img'] = soup5.find('div', class_='downloads').find('a')["href"]    
    
    # 4.3) visit URL to scrape Mars Hemisphere syrtis_major
    mars_syrtis_major_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(mars_syrtis_major_url)
    time.sleep(3)
    html = browser.html

    # create a soup object from the html
    soup6=BeautifulSoup(browser.html, 'html.parser')
    mars_dict['major_title'] = soup6.find('h2', class_='title').text
    mars_dict['major_img'] = soup6.find('div', class_='downloads').find('a')["href"] 

    # 4.4) visit URL to scrape Mars Hemisphere Valles
    mars_valles_marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(mars_valles_marineris_url)
    time.sleep(3)
    html = browser.html

    # create a soup object from the html
    soup7=BeautifulSoup(browser.html, 'html.parser')
    mars_dict['valles_title'] = soup7.find('h2', class_='title').text
    mars_dict['valles_img'] = soup7.find('div', class_='downloads').find('a')["href"] 
    
    browser.quit()
    # print(mars_dict)
    return mars_dict
    
# print(scrape()