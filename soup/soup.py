# Step 1: Install packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import time

headers = {"Accept-Language": "en-US,en;q=0.5"}

# Step 2: Start with Time measurement for scraping data
start = time.time()

# Step 3: Preparation of the storage of the scraping data
titles = []
authors = []
ratings = []
scores = []
votes = []
websites = []

# Step 4: Analysis of the URL

link = requests.get("https://www.goodreads.com/list/best_of_century/21st?id=7.Best_Books_of_the_21st_Century&page=")

bsoup = BeautifulSoup(link.text, 'html.parser')
tags = bsoup.find_all('div')[59].find_all('a')  # ], style="padding-bottom: 10px")

# Step 5:  Finding and displaying links for Best books by century
pages = np.arange(1, 2)

links = []
for tag in tags:
    #  print(tag['href'])
    links.append(tag['href'])
print(links[6:24])
links2 = links[6:24]

# Step 6:  Scraping multiple pages
print("Web scraping has begun")
for l in links2:
    for page in pages:
        page = requests.get(
            l + str(page),
            headers=headers)
        print("Scraping link: " + l)

        soup = BeautifulSoup(page.text, 'html.parser')
        book_div = soup.find_all('tr', itemtype='http://schema.org/Book')

        sleep(randint(2, 10))

# Step 7: Scraping of the selected information
        for container in book_div:
            name = container.find_all('span', role={'heading': 'name'})
            name[0] = name[0].get_text()  # potrzebne, inaczej zaciąga się nie sam tytuł, a cała linijka html do .csv
            titles.append(name)

            author = container.find_all('span', itemprop={'author': 'name'})
            author[0] = author[0].get_text()  # analogicznie
            authors.append(author)

            website = container.find_all('a', class_={'bookTitle': 'href'})
            for web in website:
                ### #   print('https://www.goodreads.com/' + web['href'])
                websites.append('https://www.goodreads.com/' + web['href'])

            rating = container.find('span', class_={'minirating'})
            # print(rating.text)
            ratings.append(rating.text)

            score = container.find_all('a', href={'#'})[0]
            for st in score:
                # print(score.text)
                scores.append(score.text)

            voted = container.find_all('a', href={'#'})[1]
            for vt in voted:
                # print(voted.text)
                votes.append(voted.text)

print("Scraping is done! Now, let's create our dataset!")

# Step 8: End with Time measurement for scraping data
stop = time.time()
print(stop - start)

# Step 9: Creating dataframes from scraping data
books = pd.DataFrame({
    'book title': titles,
    'author': authors,
    'website': websites,
    'ratings': ratings,
    'score': scores,
    'votes': votes,
})

# Display our dataframe
print(books)


# Step 10: Cleaning data using pandas

books['book title'] = books['book title'].apply(lambda x: x[0].replace('[', '').replace(']', '').replace("'", ''))

books['author'] = books['author'].apply(lambda x: x[0].replace('\n', '').replace(' (Goodreads Author)', ''))

books['votes'] = books['votes'].str.replace(',', '')
books['votes'] = books['votes'].str.extract('(\d+)').astype(int)

books['score'] = books['score'].str.replace(',', '')
books['score'] = books['score'].str.extract('(\d+)').astype(int)

books['ratings'] = books['ratings'].str.replace('really liked it ', '')  # konieczne
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
books.to_csv('books.csv')

# Step 14: Replace the zero values for the variables in the DataFrame to NaN.
books.replace(str(0), np.nan, inplace=True)
books.replace(0, np.nan, inplace=True)

# Step 15: Counting the Number of NaNs for the variables  in the DataFrame

count_nan = len(books) - books.count()
print(count_nan)

# Step 16: Some basic statistics for the variables  in the DataFrame

books.describe()

books.describe().loc[['min', 'max', 'count'], ['score', 'votes']]


# Step 17: Plotting the distributions of the variables: votes, scores, average rating

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 4))
ax1, ax2, ax3 = fig.axes
ax1.hist(books['votes'])
ax1.set_title('votes')
ax2.hist(books['score'])
ax2.set_title('score')

ax3.hist(books['average rating'])
ax3.set_title('average rating')

for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()
