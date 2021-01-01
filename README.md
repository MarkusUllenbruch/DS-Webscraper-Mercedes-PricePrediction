# Data Science Project from Scratch
## Collecting own Data with a Webscraper and implement ML price prediction of used Mercedes cars
 In this private project a complete data science pipeline is done from scratch with the following tasks:
 1. Data Collecting -- Creating my own dataset through webscraping many thousands of used Mercedes cars from mobile.de with selenium
 2. Data Cleaning/ Feature Engineering -- Creating new features out of raw data and prepare raw data for ML modeling
 3. EDA -- Explanatory Data Analysis of my collected data and findings
 4. ML Model Building -- Set up ML models for predicting the used car price with sk-learn and statsmodels

### 1. Data Collecting
The dataset was collected via webscraping the used-car selling site
[mobilde.de:](https://www.mobile.de)
specially for used Mercedes-Benz cars.
python package Selenium is used for collecting the data.

# Data Science Price Estimator of used Mercedes cars: Project Overview
* Implemented a tool that estimates prices (MAE ~ $ X K) to help customers estimate, if the price of a used car he wants to buy is fair and to help the seller side to estimate the worth of a car
* Scraped over 4000 car descriptions from mobile.de using python and selenium
* Engineered features from the text of each car name description to quantify the price value put on tags like "AMG", "G-Power", "Brabus", "BlueEfficiency" etc. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to find the best fitting model. 
* Optimized also with statsmodels 

## Code and Resources Used 
**Python Version:** 3.7 
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium

## Web Scraping
Implemented own web scraper to scrape 4000+ car offerings from mobile.com. Each car, we scaped the following content from the page:
*	Carname/ model (Automodell)
*	Price (Preis)
* Milage (Kilometerstand)
* Num Owners (Anzahl Vorbesitzer)
*	Cylinder Cubic Capacity (Hubraum)
*	Power (Leistung)
*	Fuel Type (Kraftstoffart)
*	Transmission (Getriebeart) 
*	First Registration (Erstzulassung)
*	Construction Year (Baujahr)
*	Num Seats (Anzahl Sitze)
*	Num Doors (Anzahl Türen)
*	Emmission Class (Emmissionsklasse)
*	Car Type (Autotyp zB Limousine, Coupe,.. etc)
*	Damage (Schaden)

## Data Cleaning
After scraping the data, I had to clean & feature-engineer it up so that it was usable for our Machine Learning modeling & training. Following changes were made and the following varaibles were created:

*	Parsed numeric data out of "Price"
*	Made new columns for "AMG", 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 





