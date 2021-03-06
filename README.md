# PS 239T Final Project
Jasmine Sanders: Final Project for PS 239T

## Short Description

Recent data from the National Collegiate Athletic Association (NCAA) reveals a steep decline in first-generation college athletes across nearly all Division I sports, but particularly in men’s basketball, where first-generation college athletes plunged from 28 percent in 2010 to 19 percent in 2015 (NCAA 2016). Elite high school attendance has been cited among sports journalists as increasingly playing a role in aspiring college athletes’ path to success, further widening the gap between first-generation and more advantaged student populations. Despite this assertion, there is no publicly available data that identifies NCAA players by high school type, nor have existing literatures empirically addressed this gap. This project utilizes webscraping techniques to create an original dataset that tracks high school and college characteristics of Division I men’s basketball players from 2010 to 2020. By analyzing patterns in students’ high school type (public vs. private), I can identify NCAA recruitment changes that potentially shrunk opportunities for first-generation college students. 

I used Python to scrape the ESPN Top 100 Recruiting Database (http://www.espn.com/college-sports/basketball/recruiting/playerrankings) for years 2010-2020 and exported the data to .csv. I then made a minor formatting changes in Excel and utilized Google to search student athletes' hometown and high school to determine school type: private = traditional, religious, boarding, etc.; public = traditional, charter, magnet, etc.

I then used R for data cleaning and visualization of the dataset, specifically using tidyverse, ggplot2, and knitr packages. 

## Dependencies

1. Python 3.3.6, Anaconda distribution
2. RStudio, 1.2.5033

## Files

#### Description/

1. Narrative.Rmd: Provides a brief narrative of the project, main challenges & solutions and future directions.
2. Narrative.pdf: A knitted pdf of Narrative.Rmd. 
3. Slides_Final Project Presentation.pdf: Presentation slides from 05/06/2020

#### Code/
1. 01_Final Project_Webscraping.py: Collects data from ESPN Top 100 Recruiting Data using Beautiful Soup and adds them to individual CSV files for each class.
2. 02_Final Project_Clean Visualization Data.Rmd: Loads and reformats Top 100 Dataset for bar graph visualization.
3. 03_Final Project_Visualization Script.Rmd: Conducts descriptive analysis of the data and produces a cluster bar graph for Top 100 Recruits by High School Type found in the Results directory.
4. 04_Final Project_Data Analysis and Tables.Rmd: Loads Top 100 Dataset to produce high school and college level tables found in Results directory.

#### Data/

1. Top_100_Rosters: The ESPN Top 100 Recruiting Database, available here: http://www.espn.com/college-sports/basketball/recruiting/playerrankings
2. reformatted data.csv: Contains selected data from top_100_2010-2020_csv.csv for data visualization and bar charts. 

#### Results/

1. 01_Final_Project_bar_graph.png: Clustered Bar Graph of Top 100 NCAA Recruits by High School Type from 2010-2020.
2. 02_Final_Project_line_graph.png: Grouped Line Plot displays trends in Top 100 NCAA Recruits' high school type from 2010 to 2020.
3. 03_Top producing HS.png: Table displaying the Top 10 producing high schools of NCAA Recruits from 2010-2020
4. 04_Top colleges.png: Table displaying the Top 10 colleges NCAA Recruits commit to 
