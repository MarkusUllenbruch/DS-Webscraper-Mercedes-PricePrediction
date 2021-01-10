# Project: Price Estimator of Mercedes Cars
## Collecting Data with a Webscraper and Implement a Machine Learning Pricing-System

# Table of contents
0. [Overview](#overview)
1. [Web Scraping](#scraping)
2. [Data Cleaning](#cleaning)
3. [Exploratory Data Analysis](#eda)
   - 3.1 [Findings of the Data](#findings)
   - 3.2 [Feature Selection](#selection)
4. [Modeling](#ml)
5. [Model Performance](#performance)

## 0. Overview <a name="overview"></a>
Fascinated about real-life Data-Science & ML applications and inspired by the [Machine Learning Phoenix Pricing System](https://www.daimler.com/karriere/ueber-uns/artificial-intelligence/fuer-nerds/pricing.html) from Mercedes-Benz, I thought, I could start a similar project in a small scale in order to explore and strengthen my Data Science skills.
In this project, I
- Implemented a data collection tool and webscraped over 11000+ car offerings from [mobile.de](https://www.mobile.de) using python and selenium
- Implemented a ML tool, that estimates prices (MAE ~ 8 K €) to help customers and sellers estimating the worth of a used car
- Cleaned and wrangled raw data and engineered features from existing features as preprocessing step for ML
- Automated & Optimized feature selection of Linear Regression with statsmodels.api OLS module using p-values of features
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to find the best fitting model --TO-DO--

The predictions on the training dataset (blue) and on the unseen test dataset (green) are shown below as a graph of true prices over predicted prices:
<img src="Plots/Train.png" width="350"> <img src="Plots/Test.png" width="350">

#### Code and Resources Used 
**Python Version:** 3.7 
**Packages:** pandas, numpy, sk-learn, statsmodels, tensorflow, matplotlib, seaborn, selenium

## 1. Web Scraping :floppy_disk: <a name="scraping"></a>
### [(data_collection.py)](https://github.com/MarkusUllenbruch/DS-Webscraper-Mercedes-PricePrediction/blob/main/Step1_data_collection.py)
Implemented own web scraper and scraped minimum 11000 car offerings from [mobile.de](https://www.mobile.de). Each car, I scraped the following content from the webpage:
*	Carname/ model (Automodell)
*	Price (Preis)
*  Milage (Kilometerstand)
*  Num Owners (Anzahl Vorbesitzer)
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

## 2. Data Cleaning :scissors: <a name="cleaning"></a>
### [(data_cleaning.py)](https://github.com/MarkusUllenbruch/DS-Webscraper-Mercedes-PricePrediction/blob/main/Step2_data_cleaning.py)
After scraping the data, I cleaned & feature-engineer it up so that it was usable for our Machine Learning modeling & training.
The final & cleaned dataset consists of 10 categorical features and 23 numerical features --> 108 numerical features after get dummy variables of categoricals.
Following changes were made and the following variables were created:

*	Parsed numeric data out of "Price", removed the -brutto- string
*	Removed rows without a price (price = -1)
*	Transformed "First Registration" string into numeric "Age of car"" ("06/2018" --> 1.5)
*  Fill in missing values of "power_ps" with the means of existing values of each the same car Model type
*  Remove oldtimer (> 30 years of age) rows from the data, because too specific, needing more information to predict price
*	Parsed following Car Models out of the offering description and make a "Model" column with following:
    * A-Klasse
    * C-Klasse
    * E-Klasse
    * S-Klasse
    * CLA
    * CLC
    * CLK
    * CL
    * CLS
    * SL
    * SLC
    * SLK
    * SLR
    * SLS
    * G-Klasse
    * GLA
    * GLB
    * GLC
    * GLK
    * GLE
    * M-Klasse
    * GLS
    * GL
    * X-Klasse
    * B-Klasse
    * R-Klasse
    * V-Klasse
    * Vaneo
    * Viano
* Created following new features out of existing ones:
    * AMG
    * McLaren
    * Black Series
    * Brabus
    * Carlsson
    * DC
    * G-Power
    * 63
    * 65
    * 55
    * BlueEfficiency

## 3. EDA - Exploratory Data Analysis 📊 <a name="eda"></a>
### [(EDA.ipynb)](https://github.com/MarkusUllenbruch/DS-Webscraper-Mercedes-PricePrediction/blob/main/Step3_EDA.ipynb) --CURRENTLY DOING--
Distributions of the data and some of the value counts for the categorical variables are visualized with seaborn and matplotlib. Below are a few findings from the pivot tables: 

### 3.1 Findings from the Data <a name="findings"></a>

<img src="Plots/Model.png" width="350"> <img src="Plots/price_milage2.png" width="350">
<img src="Plots/price_power_ps.png" width="350"> <img src="Plots/price_age.png" width="350">

--DESCRIPTION OF PLOTS HERE--

### 3.2 Correlation Matrix and Feature Selection <a name="selection"></a>
The correlation matrix of the numeric features are shown below:\\
<img src="Plots/corr.png" width="350">


## 4. Model Building 📈 --TO-DO-- <a name="ml"></a>
Making dummy variables out of the categorical features results in 108 numerical features in total.

I transformed all the categorical variables (like "emission_class", "Model" or "num_owners") into dummy variables with sk-learn and then split the cleaned dataset randomly up into training  and testing datasets with a test size of 20 %.   

I tried X different models and evaluated them with the metric Mean Absolute Error.  

The following models were trained:
*	**Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 
*	**Neural Network**

## 5. Model performance :white_check_mark: --TO-DO-- <a name="performance"></a>
The XYZ model outperformed the other approaches on the unseen test dataset. 
*	**Linear Regression statsmodels.api** : MAE = 8.400 €
*	**Y**: MAE = Y
*	**Z**: MAE = Z
