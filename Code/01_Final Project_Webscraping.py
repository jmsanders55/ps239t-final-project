#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:46:05 2020

@author: jasminesanders
"""
# traditional webscraping
# urlib is a standard Python library and contains functions for requesting data across the web 
from urllib.request import urlopen 
from urllib.error import HTTPError
from urllib.error import URLError

# import libraries
import requests 
from requests import get
from bs4 import BeautifulSoup
import re 
import pandas as pd
import numpy as np

from time import sleep
from random import randint

#________________________________________________________________________________________________________________________________________________________________

#specify url
for year in range(2010,2021):
    print(year)
    url='http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/'+str(year)+'/order/true'
    print(url)
# query the website and return the html to the variable 'page'    
    try:
        page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/'+str(year)+'/order/true')
    except HTTPError as e:
        print(e) # The HTTP error: "404 Page Not Found (you messd up)" or 500 Internal Server Error (I messed up)"
    except URLError as e:
        print("The server is broken") # No server could be reached 
    else:
        print("The site is working")

#________________________________________________________________________________________________________________________________________________________________       
# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

# find results for even rows within table
roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)
  
# find results for odd rows within table  
roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Extracted table elements are url links, thus I will need to create a new list to loop through to find all urls for both even and odd rows

##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
        
print(all_even_urls)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)


#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
print(hometown)
print(school)    
print(position)
print(status)

div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2020.csv")

#______________________________________________________________________________________________________________________________________________________________________
##Continue loop for remaining years

# While I set up the code to string for year in the webpage, I was unable to scrape multiple pages in one data frame. I tried to scrape using the sleep() function from the time module and the randint() function from the random module but neither work. For the sake of this project, I just re-ran the code changing the years to scrape data and write to a csv. Moving forward, I will revisit this to ascertain how to revise code to scrape from multiple websites.  
#____________________________________________________________________________________________________________________________________________________________________
###Class of 2019

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2019/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2019.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2018

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2018/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2018.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2017

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2017/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2017.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2016

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2016/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2016.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2015

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2015/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2015.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2014

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2014/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2014.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2013

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2013/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2013.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2012

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2012/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2012.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2011

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2011/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2011.csv")

#____________________________________________________________________________________________________________________________________________________________________
###Class of 2010

page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2010/order/true')

# parse the html using beautiful soup and store in variable 'soup' and extract table elements 
soup = BeautifulSoup(page, "html.parser")

roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)

roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Create new list that merges even and odd urls
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href') # go to link and extract website
        print(url)
        all_even_urls.append(url)
#____________________________________________________________________________________________________________________________________________________________________________________
##Create list for data frame

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls: # loop over results

    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find elements  
                    {'class':'bio'})
    for a in bio.findAll('a'): # clean/remove unnecessary text
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterate through each row
    if len(cells) == 4: # no heading 
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) 
        school.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        position.append(cells[2].find_all(text=re.compile('[A-Z]+')))
        status.append(cells[3].find_all(text=re.compile('[A-Z]+')))
    else:
        print("something is wrong") # for debugging
    bio_list.append(bio)
  
div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

# Create CSV
div_pd.to_csv("top_100_2010.csv")