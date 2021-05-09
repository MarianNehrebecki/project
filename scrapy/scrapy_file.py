# 1. importing necessary libraries
import scrapy
import pandas as pd
import time

# 2. creating our spider

class Book(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    avgrating = scrapy.Field()
    score = scrapy.Field()
    votes = scrapy.Field()
    website = scrapy.Field()


class BooksSpider(scrapy.Spider):
    name = 'books'

#start_urls -> links we want to scrap
    start_urls = [
        'https://www.goodreads.com/list/show/7.Best_Books_of_the_21st_Century?page=1',
        'https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century?page=1',
        "https://www.goodreads.com/list/show/16.Best_Books_of_the_19th_Century?page=1",
        "https://www.goodreads.com/list/show/30.Best_Books_of_the_18th_Century?page=1",
        "https://www.goodreads.com/list/show/53.Best_Books_of_the_17th_Century?page=1",
        "https://www.goodreads.com/list/show/52.Best_Books_of_the_16th_Century?page=1",
        "https://www.goodreads.com/list/show/74.Best_Books_of_the_15th_Century?page=1",
        "https://www.goodreads.com/list/show/73.Best_Books_of_the_14th_Century?page=1",
        "https://www.goodreads.com/list/show/1384.Best_Books_of_the_13th_Century?page=1",
        "https://www.goodreads.com/list/show/71.Best_Books_of_the_12th_Century?page=1",
        "https://www.goodreads.com/list/show/1414.Best_Books_of_the_11th_Century?page=1",
        "https://www.goodreads.com/list/show/14.Best_Books_of_the_10th_Century?page=1",
        "https://www.goodreads.com/list/show/8163.Best_Books_of_the_9th_Century?page=1",
        "https://www.goodreads.com/list/show/4088.Best_Books_of_the_8th_Century?page=1",
        "https://www.goodreads.com/list/show/71525.Best_Books_of_the_7th_Century?page=1",
        "https://www.goodreads.com/list/show/3079.Best_Books_of_the_6th_Century?page=1",
        "https://www.goodreads.com/list/show/3078.Best_Books_of_the_5th_Century?page=1",
        "https://www.goodreads.com/list/show/3077.Best_Books_of_the_4th_Century?page=1"
    ]

    def parse(self, response):
        b = Book() #creates an object of class Book

        #century_xpath = '//html/body/div[2]/div[3]/div[1]/div[2]/div[3]/h1/text()' #scrapes data on the century
        title_xpath = '//td[3]/a/span/text()' #scrapes data on the title of the book
        author_xpath = '//td[3]/span[2]/div/a/span/text()' #scrapes data on the author of the book
        avgrating_xpath = '//td[3]/div[1]/span/span/text()' #scrapes data on the average user rating
        score_xpath = '//td[3]/div[2]/span/a[1]/text()' #scrapes data on the score
        votes_xpath = '//td[3]/div[2]/span/a[2]/text()' #scrapes data on the votes
        website_xpath = '//td[3]/a/@href' #scrapes data on the website - link to the book's profile

        b['title'] = response.xpath(title_xpath).extract()
        b['author'] = response.xpath(author_xpath).extract()
        b['avgrating'] = response.xpath(avgrating_xpath).extract()
        b['score'] = response.xpath(score_xpath).extract()
        b['votes'] = response.xpath(votes_xpath).getall()
        b['website'] = response.xpath(website_xpath).getall()

        yield b

# terminal command for easy access: scrapy crawl books -o plik.csv
