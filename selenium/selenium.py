# Step 1: Install packages

import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By
from time import sleep
from random import randint

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Step 2: Start with Time measurement for scraping data
start = time.time()

# Step 3: Analysis of the URL

driver = webdriver.Chrome(ChromeDriverManager().install())
link = "https://www.goodreads.com/list/best_of_century/21st?id=7.Best_Books_of_the_21st_Century&page="
driver.get(link)

pages = np.arange(1, 2)

# Step 4:  Finding and displaying links for Best books by century

incategory = driver.find_elements_by_class_name("mediumText")
# Generate a list of links for each century
links = []
for i in incategory:
    # Get the href property
    a = i.find_elements(By.TAG_NAME, 'a')
    # Append the link to list links
    for el in a:
        links.append(el.get_attribute("href"))
print(links[6:24])
links2 = links[6:24]

# Step 5:  Scraping multiple pages
print("Web scraping has begun")

# Step 6: Preparation of the storage of the scraping data
element_list = []

for link in links2:
    for page in pages:
        page_ = driver.get(link)
        print("Scraping link: " + link)
        sleep(randint(1, 2))
# Step 7: Scraping of the selected information
        try:
            titles = driver.find_elements_by_class_name("bookTitle")
            time.sleep(0.5)
            authors = driver.find_elements_by_class_name("authorName")
            time.sleep(0.5)
            ratings = driver.find_elements_by_class_name("minirating")
            time.sleep(0.5)
            scores = driver.find_elements_by_partial_link_text("score:")
            time.sleep(0.5)
            votes = driver.find_elements_by_partial_link_text("voted")
            time.sleep(0.5)
        except (selenium.common.exceptions.StaleElementReferenceException, IndexError):
            continue
        length = len(titles)
        if len(authors) != length or len(ratings) != length or len(scores) != length or len(votes) != length:
            continue
        for i in range(length):
            href = titles[i].get_attribute("href")
            element_list.append(
                [titles[i].text, authors[i].text, ratings[i].text, scores[i].text, votes[i].text, href])

print("Scraping is done! Now, let's create our dataset!")

# Step 8: End with Time measurement for scraping data
stop = time.time()
print(stop-start)

# Step 9: Creating dataframes from scraping data
books = pd.DataFrame(element_list)
# We introduce the name of the column
books.columns = ['titles', 'authors', 'ratings', 'scores', 'votes', 'website']
# Display our dataframe
print(books)

# Step 10: Cleaning data using pandas

books['votes'] = books['votes'].str.replace(',', '')
books['votes'] = books['votes'].str.extract('(\d+)').astype(int)

books['scores'] = books['scores'].str.replace(',', '')
books['scores'] = books['scores'].str.extract('(\d+)').astype(int)

books['ratings'] = books['ratings'].str.replace('really liked it ', '')
books['ratings'] = books['ratings'].str.replace(',', '')

books['average rating'] = books['ratings'].apply(lambda x: x.split()[0])
books['average rating'] = books['average rating'].str.replace('really', '')
books['average rating'] = books['average rating'].str.replace('it', '')
books['average rating'] = books['average rating'].str.replace('liked', '')

books['average rating'] = pd.to_numeric(books['average rating'], errors='coerce')

books.drop("ratings", axis = 1, inplace = True)

# Step 11: Display the data types of the variables
print(books.dtypes)

# Step 12: Verifying missing data
print(books.isnull().sum())

# Step 13: Save the scraping data into a CSV file
books.to_csv("books_selenium.csv")


# Step 14: Replace the zero values for the variables in the DataFrame to NaN.
books.replace(str(0), np.nan, inplace=True)
books.replace(0, np.nan, inplace=True)

# Step 15: Counting the Number of NaNs for the variables in the DataFrame

count_nan = len(books) - books.count()
print(count_nan)

time.sleep(3)
driver.close()

# Step 16: Some basic statistics for the variables  in the DataFrame

books.describe()


# Step 17: Plotting the distributions of the variables: votes, scores, average rating

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes
ax1.hist(books['votes'])
ax1.set_title('votes')
ax2.hist(books['scores'])
ax2.set_title('scores')

ax3.hist(books['average rating'])
ax3.set_title('average rating')

for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()
