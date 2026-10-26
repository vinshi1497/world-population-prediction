# 🌍 World Population Prediction

## Project Overview

This project performs statistical analysis and machine learning on a country-wise population dataset. The dataset is collected through web scraping and contains demographic, geographic, and population-related information for countries around the world.

The project includes:

- Data collection using web scraping
- Data cleaning and preprocessing
- Descriptive statistical analysis
- Population distribution analysis
- Log transformation of population
- Sampling distribution analysis
- Confidence interval estimation
- One-sample t-test
- Covariance analysis
- Pearson correlation
- Spearman correlation
- Machine learning model training
- Model evaluation and comparison
- Model saving using Joblib
- Interactive population prediction using Streamlit

---

## Dataset

The dataset contains country-wise population and demographic information, including:

- Country
- Population
- Yearly Population Change
- Net Population Change
- Population Density
- Land Area
- Net Migrants
- Fertility Rate
- Median Age
- Urban Population
- World Population Share

The dataset is collected from Worldometer using Python web scraping with `Requests` and `BeautifulSoup`.

The cleaned dataset is stored as:

```text
population_cleaned.csv
```

---

## Technologies Used

| Tool / Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Development and experimentation |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Matplotlib | Data visualization |
| SciPy | Statistical analysis and hypothesis testing |
| Scikit-learn | Machine learning |
| Requests | Web scraping |
| BeautifulSoup4 | HTML parsing and web scraping |
| Joblib | Saving and loading trained models |
| Streamlit | Interactive web application |

---

## Project Workflow

```text
Worldometer Population Data
            ↓
       Web Scraping
            ↓
     Data Collection
            ↓
      Data Cleaning
            ↓
  Statistical Analysis
            ↓
   Data Visualization
            ↓
   Hypothesis Testing
            ↓
  Correlation Analysis
            ↓
     Feature Selection
            ↓
      Train/Test Split
            ↓
    Machine Learning
            ↓
     Model Evaluation
            ↓
      Best Model
            ↓
       Joblib (.pkl)
            ↓
      Streamlit App
            ↓
   Population Prediction
```

---

## Statistical Analysis

The project performs descriptive statistical analysis on the population dataset.

The following measures are calculated:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Quartiles
- Minimum and maximum values

The project also analyses the distribution of population values.

Because population values are highly right-skewed, a logarithmic transformation is applied:

```python
df["log_Population"] = np.log(df["Population_2026"])
```

The transformed population is then used for statistical analysis and machine learning.

---

## Sampling Distribution

Random samples are generated from the log-transformed population data.

A sample size of 30 is used to generate multiple sample means and study the sampling distribution of the mean.

Different sample sizes are also compared to observe how sample size affects the sampling distribution.

---

## Hypothesis Testing

A one-sample t-test is performed on the log-transformed population data.

The hypothesized mean corresponds to a population of:

```text
10,000,000
```

The hypothesis is tested using a significance level of:

```text
α = 0.05
```

The null hypothesis is rejected when:

```text
p-value < 0.05
```

Otherwise, the null hypothesis is not rejected.

---

## Correlation Analysis

The project also analyses relationships between numerical variables using:

### Covariance

Covariance is used to determine the direction of the relationship between two variables.

### Pearson Correlation

Pearson correlation measures the strength and direction of a linear relationship between two numerical variables.

### Spearman Correlation

Spearman correlation measures the strength and direction of a monotonic relationship using ranked values.

---

## Machine Learning

The cleaned dataset is used to build a machine learning model for population prediction.

The target variable is:

```text
log_Population
```

The model uses the following features:

```text
Density_P_Km2
Land_Area_Km2
Fert_Rate
Median_Age
Urban_Pop_%
Migrants_Net
Yearly_Change_%
```

The data is divided into training and testing sets using:

```text
80% Training
20% Testing
```

---

## Model Evaluation

The machine learning model is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The actual and predicted log population values are also visualized using an Actual vs Predicted plot.

The best-performing model is selected based on the model comparison results.

---

## Model Saving

The trained model is saved using Joblib.

The project saves:

```text
best_population_model.pkl
```

This file contains the trained machine learning model.

The feature names used by the model are saved separately as:

```text
population_feature_columns.pkl
```

These files allow the trained model to be loaded later without retraining it.

---

## Streamlit Deployment

The trained model is deployed using Streamlit.

The Streamlit application is contained in:

```text
app.py
```

The application loads the saved model and feature columns:

```python
model = joblib.load("best_population_model.pkl")
feature_cols = joblib.load("population_feature_columns.pkl")
```

The user enters the required demographic and geographic information through the web interface.

The application then:

1. Collects the input values
2. Creates a DataFrame using the trained model's feature columns
3. Generates the predicted log population
4. Converts the prediction back to the original population scale using `np.exp()`
5. Displays the estimated population

---

## Streamlit Inputs

The application accepts:

| Input | Description |
|---|---|
| Population Density | People per km² |
| Land Area | Total land area in km² |
| Fertility Rate | Average fertility rate |
| Median Age | Median age of the population |
| Urban Population | Percentage of population living in urban areas |
| Net Migrants | Net migration value |
| Yearly Population Change | Annual population change percentage |

The output is:

```text
Predicted Population
```

---

## Project Files

The GitHub repository contains:

```text
population-prediction/
│
├── app.py
├── best_population_model.pkl
├── population_feature_columns.pkl
├── population_cleaned.csv
├── SI_Lab_Project.ipynb
├── requirements.txt
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `app.py` | Streamlit deployment application |
| `best_population_model.pkl` | Saved trained machine learning model |
| `population_feature_columns.pkl` | Saved feature-column information |
| `population_cleaned.csv` | Cleaned dataset |
| `SI_Lab_Project.ipynb` | Complete Google Colab implementation |
| `requirements.txt` | Python dependencies required for deployment |
| `README.md` | Project documentation |

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd population-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## Prediction Process

```text
User Input
    ↓
Streamlit Interface
    ↓
Input DataFrame
    ↓
Saved Machine Learning Model
    ↓
Predicted log(Population)
    ↓
Exponential Transformation
    ↓
Predicted Population
```

---

## Conclusion

The project demonstrates how statistical analysis and machine learning can be applied to real-world population data.

The workflow begins with web scraping and data preprocessing, followed by statistical analysis, hypothesis testing, correlation analysis, and machine learning. The trained model is saved using Joblib and integrated into a Streamlit application, allowing users to enter demographic information and obtain a population prediction through an interactive interface.
