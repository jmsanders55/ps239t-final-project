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
#
#________________________________________________________________________________________________________________________________________________________________

import requests 

for year in range(2010,2021):
    print(year)
    url='http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/'+str(year)+'/order/true'
    print(url)
    
    try:
        page = urlopen('http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/'+str(year)+'/order/true')
    except HTTPError as e:
        print(e) # The HTTP error: "404 Page Not Found (you messd up)" or 500 Internal Server Error (I messed up)"
    except URLError as e:
        print("The server is broken") # No server could be reached 
    else:
        print("The site is working")

#________________________________________________________________________________________________________________________________________________________________
        
#Insert beautiful soup code 
from bs4 import BeautifulSoup
    
soup = BeautifulSoup(page, "html.parser")

#________________________________________________________________________________________________________________________________________________________________    
### Extracting a table
    #Pattern find_all(tagName, tagAttributes)
roster_even_table = soup.findAll('tr',
                                {'class':'evenrow'})
print(roster_even_table)
    
roster_odd_table = soup.findAll('tr',
                                {'class':'oddrow'})
print(roster_odd_table)
    
#________________________________________________________________________________________________________________________________________________________________________________
##Code for new data set 
##or just keep adding to a dataframe
all_even_urls=[] 

for i in range(0,50):
        #print(i)
        url = roster_even_table[i].find('a').get('href')
        print(url)
        all_even_urls.append(url)
        
print(all_even_urls)

all_odd_urls=[]    
for i in range(0,50):
        #print(i)
        url=roster_odd_table[i].find('a').get('href')
        print(url)
        all_even_urls.append(url)


#____________________________________________________________________________________________________________________________________________________________________________________
##Create list
##
import re 

bio_list = []
hometown = []  
school = []
position = []
status = []  

for url in all_even_urls:
    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    bio = page.find('div', # find element  
                    {'class':'bio'})
    for a in bio.findAll('a'):
        a.replaceWithChildren()
    for section in bio.findAll('ul'): 
        cells = section.findAll(['li']) # to iterater through each row
    if len(cells) == 4: # no heading
        hometown.append(cells[0].find_all(text=re.compile('[A-Z]+'))) # there's only string 
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

import pandas as pd # convention

div_pd = pd.DataFrame() # create a data frame
div_pd['hometown'] = hometown
div_pd['high school'] = school
div_pd['position'] = position
div_pd['status'] = status

print(div_pd)

div_pd.to_csv("top_100_2020.csv")

#______________________________________________________________________________________________________________________________________________________________________
##Continue loop for remaining years

    