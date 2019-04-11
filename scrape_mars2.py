import os
from bs4 import BeautifulSoup as bs
import requests


nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

response = requests.get(nasa_url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())


titles = soup.find_all('div', class_= "content_title")
shortp = soup.find_all('div', class_="rollover_description_inner")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(titles[0].text)
print(shortp[0].text)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

from splinter import Browser

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
browser.click_link_by_partial_text('FULL IMAGE')
soup2 = bs(html, 'html.parser')
image_url = soup2.find('a', class_='button fancybox')
image_url2 = image_url.get('data-fancybox-href')
base_url = 'https://www.jpl.nasa.gov'
featured_image_url = print(f"{base_url}{image_url2}")
featured_image_url

twit = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(twit)
soup3 = bs(response.text, 'html.parser')

latest_twit = soup3.find('div', class_ = "js-tweet-text-container")
latest_twitting = latest_twit.find('p')
latester_twitting = latest_twitting.find('a')
latester_twitting.extract()
mars_weather = latest_twitting.text.strip()

import pandas as pd

facts = 'https://space-facts.com/mars/'
fact_table = pd.read_html(facts)


fact_table_df = fact_table[0]
fact_table_df.columns=["Feature","Value"]
fact_table_df.set_index("Feature", inplace = True)

html_table = fact_table_df.to_html()

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


hemispher_image_urls = []
for c in range(0, 4):
    html = browser.html
    soup = bs(html, 'html.parser')
    click = soup.find_all('div', class_='item')
    click_href = click[c].a.get('href')
    s = pd.Series(['https://astrogeology.usgs.gov',click_href])
    href = s.str.cat()
    response = requests.get(href)
    soup_next = bs(response.text, 'html.parser')
    down = soup_next.find('div', class_ = "downloads")
    the_a = down.find_all('a')
    orig = the_a[1].get('href')
    name = soup_next.find('h2', class_= "title").text
    d1 = {"title": name, "img_url":orig}
    hemispher_image_urls.append(d1)

