# Scraping Goodreads with python
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Instruction how to run the scrapers](#Instruction-how-to-run-the-scrapers)
  - [Scrapers](#Scrapers)
  - [Short technical description of the scraper](#Short-technical-description-of-the-scraper)
  - [Setup](#setup)
  - [Desired output](#Desired-output)



## General info
* The project was created as part of Webscraping and Social Media Scraping subject. 
* With a few lines of code (with different levels of complicated of course) we will hopefully be able to scrape the desired data. Our target is the Goodreads website (books’ rating and recommendations) and basic data on books.
* Goodreads is an imdb of the book world. It is a place for book lovers to rate, find and review books. The website provides information on books and user ratings. It also contains a classification on best books of the century, by user ratings. This is our target.

	
## Technologies
Project is created with:
* Python 3.6

## Instruction how to run the scrapers


### Scrapers
We scraped the desired data from the Goodreads website using Python language and applied three different methods:
* beautiful soup (see: folder soup, file soup.py),
* scrapy (see: folder scrapy, file scrapy_file.py and folder additional_scrapy, file scrapy_data_reader_im-not-a-spider.py),
* selenium (see: folder selenium, file selenium.py).

* GitHub repository contains three separate folders which, respectively, contain all files required to run each of the scrapers (scrapy folder contains the additional file for reading the data!).

### Short technical description of the scraper
1.	Import packages
2.	Preparation of the storage of the scraping data
3.	Analysis of the URL
4.	Scraping multiple pages 
5.	Cleaning data 
6.	Checking missing data
7.	Time measurement for scraping data

	
### Setup
To run this project, install it locally using terminal:

```
$ pip install beautifulsoup4
$ pip install selenium
$ pip install webdriver_manager
$ pip install Scrapy
```


### Desired output	
We decided to scrape the information on Best books by century. The following information on each book was scraped:
* title of the book,
* author of the book,
* website - link to the book’s website on Goodreads,
* average rating – average rating of the book from the users,
* score,
* number of votes.



