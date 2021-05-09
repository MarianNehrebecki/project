# Scraping Goodreads with python
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
* The project was created as part of Webscraping and Social Media Scraping subject. 
* With a few lines of code (with different levels of complicated of course) we will hopefully be able to scrape the desired data. Our target is the Goodreads website (books’ rating and recommendations) and basic data on books.
* Goodreads is an imdb of the book world. It is a place for book lovers to rate, find and review books. The website provides information on books and user ratings. It also contains a classification on best books of the century, by user ratings. This is our target.

	
## Technologies
Project is created with:
* Python 3.6
	
## Setup
To run this project, install it locally using npm:

```
$ pip install beautifulsoup4
$ pip install selenium
$ pip install webdriver_manager
$ pip install Scrapy
```

## Desired output	
* We decided to scrape the information on Best books by century. The following information on each book was scraped:
•	title of the book,
•	author of the book,
•	website - link to the book’s website on Goodreads,
•	average rating – average rating of the book from the users,
•	score,
•	number of votes.
