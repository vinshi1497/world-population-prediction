# World Population Prediction

## Project Overview

This project performs statistical analysis and machine learning on world population data.

The dataset contains population-related attributes for countries around the world, including population, population change, population density, land area, fertility rate, median age, urban population and net migration.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SciPy
- BeautifulSoup
- Requests
- Joblib
- Gradio
- Google Colab

## Project Components

- Data collection using web scraping
- Data cleaning and preprocessing
- Descriptive statistical analysis
- Data distribution analysis
- Log transformation
- Sampling distribution
- Point estimation
- Standard error
- One-sample t-test
- Covariance analysis
- Pearson correlation
- Spearman correlation
- Regression modelling
- Model evaluation
- Gradio GUI deployment

## Files

| File | Description |
|---|---|
| `SI_Lab_Project.ipynb` | Complete Google Colab notebook |
| `population.csv` | Original collected dataset |
| `population_cleaned.csv` | Cleaned dataset |
| `population_model.joblib` | Trained machine learning model |
| `app.py` | Gradio GUI application |

## Dataset

The population dataset was collected from Worldometers:

https://www.worldometers.info/world-population/population-by-country/

## Model Evaluation

The project evaluates the regression model using:

- MAE
- MSE
- RMSE
- R² Score

## GUI

A Gradio-based interface is provided for predicting population based on population-related input features.

## How to Run

Install the required libraries:

```bash
python app.py

