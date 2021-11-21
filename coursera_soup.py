from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests
import csv
import time

s = Service('/Users/cindyhuang/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)


base_url = "https://www.coursera.org/courses"

desired_skill = input('Please enter skills to search: ').split(" ")

per20Skills = "%20".join(desired_skill)

courseraUrl = "https://www.coursera.org/search?query=" + per20Skills

driver.get(courseraUrl)
timeout = 20

try:
    WebDriverWait(driver, timeout)

except TimeoutException:
    driver.quit()


html_soup = BeautifulSoup(driver.page_source, "html.parser")

# # find course title tag and class
# found = html_soup.find("h2", {'class': "cds-1 card-title css-iyr9nj cds-3"})
# # find course url tag and class
# foundU = html_soup.find("a", {'class': "result-title-link"})

found_all = html_soup.find_all("h2", {'class': "cds-1 card-title css-iyr9nj cds-3"})
foundU_all = html_soup.find_all("a", {'class': "result-title-link"})

# Create dictionary for course name and url
dict_course = dict()

with open('coursera.csv', 'w+', newline='') as f:
    Fields = ['Course Name', 'Course Url']
    writer = csv.DictWriter(f, fieldnames=Fields)
    writer.writeheader()

    for i in range(len(found_all)):
        # for course urls
        toUrl = foundU_all[i].get('href')
        courseraUrl = base_url + toUrl

        # store info in dictionary Course Name -> Course Url
        dict_course[found_all[i].text] = courseraUrl
        writer.writerow({'Course Name': found_all[i].text, 'Course Url': courseraUrl})













