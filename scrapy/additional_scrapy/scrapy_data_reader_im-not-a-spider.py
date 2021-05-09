# 1. importing necessary packages
import csv
import pandas as pd
import regex as re

# 2. opening the scrapy output
f = open("plik.csv", 'r') #please provide a correct file name
f # it is a buffered text stream
data = f.read() # read the buffer into data
#print(data) # print the data
columns = re.split('","|"\n"',data) #splitting into seperate lists
#print(columns[0])
#print(columns[1])
#print(columns[2])
#print(columns[3])
#print(columns[4])
#print(columns[5])

# 3. cleaning the data

one = columns[0].split(',') #splitting the first column to get headers and authors
#print(one)

headers = one[0:6] #creating headers
headers[5] = headers[5][:7] #cleaning the data
print(headers)

#creating columns from lists for each variable # only for first two centuries scraped - the logic can be followed for the rest
authors = one[6:] +columns[6].split(',') 
authors[0]=authors[0][9:]
avgrating = columns[1].split('ratings') + columns[7].split('ratings')  
#century = columns[2].split(',') +columns[9].split(',') 
score = columns[2].split(',score:') + columns[8].split(',score:')
#title = columns[3].split(',')
title = re.split(',(?![+ ])',columns[3]) + re.split(',(?![+ ])',columns[9])
votes = columns[4].split('voted,') + columns[10].split('voted,')
website = columns[5].split(',') + columns[11].split(',')
#print(headers)
#print(authors)
#print(avgrating)
#print(score)
#print(title)
#print(votes)

# 4. adding the split data into separate lists 
list=[]

list.append(authors)
list.append(avgrating)
#list.append(century)
list.append(score)
list.append(title)
list.append(votes)
list.append(website)

# 5. creating a dataframe

print(list)
books = pd.DataFrame(list, index=[headers]).T

print(books)

# 6. export to .csv

books.to_csv('scrapybooks.csv')
