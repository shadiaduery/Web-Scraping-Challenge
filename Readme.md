web-scraping-challenge: Mission to Mars

Tools Used:
Jupyter Notebook
MongoDB
Flask App
Following Libraries:
- import pandas as pd
- from pprint import pprint
- from splinter import Browser
- from bs4 import BeautifulSoup
- from selenium import webdriver
- from selenium.webdriver.chrome.options import Options
- import time


Background
The task requested was to go to designated website (NASA), and scrape specific information from several landing pages provided. The intention was to prove proficiency in finding elements on any website's html code. The elements scrapped for this assigment were: A Title, A Paragraph, A Table, and Five images. 

Step 1: Scraping
Four landing web pages were provided to scrape the following information:
The latest news title
The latest news paragraph text
JPL Featured Space Image
Mars Four Hemispheres Images

To complete this step a Jupyter Notebook and all the libraries mentioned above were used. 

All the requested information was saved as a dictionary and as a list to test which one would work better to import the information on the next steps

Step 2: MongoDB and Flask Application
All the code written to scrape the requested information done in a jupyter notebook was copy pasted to a .py file to be readed in VS Code. The .py file has a scrape fuction to be called from another file if needed.

An app.py file was created to call the scrape fuction of from the .py file, then code was written to create a connection to MongoDB, store the scraped information, and be called back to render on a index.html file created. 

The index.html file was styled using Bootstrap script. Once styled the index.html the scraped information stored on MongoDB was rendered on specific places of the index.html file.

Once the index.html was fully running two screen shots picture were taken and stored on the Image folder of this repo to show the final product. 