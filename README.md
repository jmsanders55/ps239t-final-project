# ps239t-final-project
Jasmine Sanders: Final Project for PS 239T

## Short Description

Recent data from the National Collegiate Athletic Association (NCAA) reveals a steep decline in first-generation college athletes across nearly all Division I sports, but particularly in men’s basketball, where first-generation college athletes plunged from 28 percent in 2010 to 19 percent in 2015 (NCAA 2016). Elite high school attendance has been cited among sports journalists as increasingly playing a role in aspiring college athletes’ path to success, further widening the gap between first-generation and more advantaged student populations. Despite this assertion, there is no publicly available data that identifies NCAA players by high school type, nor have existing literatures empirically addressed this gap. This project utilizes webscraping techniques to create an original dataset that tracks high school and college characteristics of Division I men’s basketball players from 2010 to 2020. By analyzing patterns in students’ high school type (public vs. private), I can identify NCAA recruitment changes that potentially shrunk opportunities for first-generation college students. 

## Dependencies

List what software your code depends on, as well as version numbers, like so:.

1. R, 3.6.1

In your scripts, includes commands that `require()` packages.

## Files

List all files (other than `README.md` and `Final-Project.RProj`) contained in the repo, along with a brief description of each one, like so:

#### /

1. Narrative.Rmd: Provides a 3-5 page narrative of the project, main challenges, solutions, and results.
2. Narrative.pdf: A knitted pdf of 00_Narrative.Rmd. 
3. Slides.XXX: Your lightning talk slides, in whatever format you prefer.

#### Code/
1. 01_collect-nyt.R: Collects data from New York Times API and exports data to the file nyt.csv
2. 02_merge-data.R: Loads, cleans, and merges the raw Polity and NYT datasets into the Analysis Dataset.
3. 03_analysis.R: Conducts descriptive analysis of the data, producing the tables and visualizations found in the Results directory.

#### Data/

1. polity.csv: The PolityVI dataset, available here: http://www.systemicpeace.org/inscrdata.html
2. nyt.csv: Contains data from the New York Times API collected via collect-nyt.ipynb . Includes information on all articles containing the term "Programmer Cat", 1980-2010.
3. analysis-dataset.csv: The final Analysis Dataset derived from the raw data above. It includes country-year values for all UN countries 1980-2010, with observations for the following variables: 
    - *ccode*: Correlates of War numeric code for country observation
    - *year*: Year of observation
    - *polity*: PolityVI score
    - *nyt*: Number of New York Times articles about "Programmer Cat"

#### Results/

1. coverage-over-time.jpeg: Graphs the number of articles about each region over time.
2. regression-table.txt: Summarizes the results of OLS regression, modelling *nyt* on a number of covariates.

## More Information

Include any other details you think your user might need to reproduce your results. You may also include other information such as your contact information, credits, etc.
