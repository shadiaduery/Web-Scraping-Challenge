Web-Scraping-Challenge: Mission to Mars 
By : Shadia Duery 
Date: 12/22/2020

Tools Used:
-Jupyter Notebook
-MongoDB
-Flask App

Following Libraries:
- import pandas as pd
- from pprint import pprint
- from splinter import Browser
- from bs4 import BeautifulSoup
- from selenium import webdriver
- from selenium.webdriver.chrome.options import Options
- import time

Background:
- The task requested was to scrape specific information from a designated website (NASA)
- The intention was to prove proficiency in finding elements on any website's html code
- The elements scrapped for this assigment were: A Title, A Paragraph, A Table, and Five images
- Store the scraped information on an online Database (MongoDB)
- Retrieve the stored information and render it into a newly design html landing page

Step 1: Scraping
Four landing web pages were provided to scrape the following information:
- The latest news title
- The latest news paragraph text
- JPL Featured Space Image
- A table with Mars data
- Mars Four Hemispheres Images

To complete this step a Jupyter Notebook was created and all the libraries mentioned above were imported in it.
All the requested information was saved as a dictionary and as a list to test which one would work better to import the information on the next steps

Step 2: MongoDB and Flask Application
All the code written to scrape the requested information done in a jupyter notebook was copy pasted to a .py file to be read in VS Code. The .py file had a scrape fuction to be called from another file if needed.

An app.py file was created to call the scrape fuction from the mars_scrape.py file, then code was written to create a connection to MongoDB, created  and stored the collection of scraped information to be later called and rendered into the previously created and styled index.html file.

The html file was styled using Bootstrap script. 

Once the index.html was fully running two screen shots picture were taken and stored on the Image folder of this repo to show the final product. 