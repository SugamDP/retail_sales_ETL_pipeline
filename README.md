# Retail Sales ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline built using **Python, Pandas, SQLAlchemy, and MySQL**.

The project extracts retail sales data from CSV files, cleans and transforms the data into fact and dimension tables, loads the transformed data into a MySQL database, and uses SQL queries to perform sales analysis.

## Project Overview

The goal of this project is to demonstrate a basic data engineering workflow by converting raw retail datasets into structured tables that can be used for analytical queries.

The pipeline follows three main stages:

1. **Extract** — Load raw CSV datasets using Pandas.
2. **Transform** — Clean the data and create fact and dimension tables.
3. **Load** — Load the transformed datasets into MySQL using SQLAlchemy.

### ETL Flow

```text
CSV Files
    |
    v
Extract
(Pandas)
    |
    v
Transform
(Cleaning + Data Modeling)
    |
    v
Fact & Dimension Tables
    |
    v
Load
(SQLAlchemy + PyMySQL)
    |
    v
MySQL
    |
    v
SQL Analysis
```

## Tech Stack

- **Python**
- **Pandas**
- **SQLAlchemy**
- **PyMySQL**
- **MySQL**
- **SQL**

## Project Structure

```text
retail_sales_ETL_pipeline/
│
├── csv_files/
│   ├── Features.csv
│   ├── sales.csv
│   └── stores.csv
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── query/
│   └── queries.sql
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The project uses retail sales data containing information about stores, departments, weekly sales, dates, holidays, and economic factors.

The source data is divided into three datasets:

### Sales

Contains weekly sales information for different stores and departments.

Important fields include:

- `Store`
- `Dept`
- `Date`
- `Weekly_Sales`
- `IsHoliday`

### Stores

Contains information about individual stores.

Important fields include:

- `Store`
- `Type`
- `Size`

### Features

Contains additional store and economic information for different dates.

Important fields include:

- `Store`
- `Date`
- `Temperature`
- `Fuel_Price`
- `CPI`
- `Unemployment`
- `IsHoliday`

Markdown-related columns from the original dataset are removed during the transformation process.

## Data Model

The transformation stage organizes the data into fact and dimension tables.

### `fact_sales`

Contains the main sales measurements.

Fields include:

- Store
- Department
- Date
- Weekly Sales
- Holiday indicator

### `dim_store`

Contains descriptive information about each store.

Fields include:

- Store
- Type
- Size

### `dim_date`

Contains date-related attributes used for time-based analysis.

Fields include:

- Date
- Holiday indicator
- Year
- Month
- Week
- Day

### `dim_feature`

Contains external and economic factors associated with stores and dates.

Fields include:

- Store
- Date
- Temperature
- Fuel Price
- CPI
- Unemployment
- Holiday indicator

## ETL Process

### 1. Extract

The extraction stage reads the source CSV files into Pandas DataFrames.

```python
import pandas as pd

features_df = pd.read_csv("csv_files/Features.csv")
sales_df = pd.read_csv("csv_files/sales.csv")
stores_df = pd.read_csv("csv_files/stores.csv")
```

### 2. Transform

The transformation stage cleans and restructures the extracted data.

Transformations include:

- Converting date columns to appropriate datetime values
- Removing unnecessary markdown columns
- Removing duplicate records where appropriate
- Creating store dimension data
- Creating date dimension attributes
- Creating feature dimension data
- Creating the sales fact table

Example date attributes:

```python
dim_date["year"] = dim_date["Date"].dt.year
dim_date["month"] = dim_date["Date"].dt.month
dim_date["week"] = dim_date["Date"].dt.isocalendar().week.astype(int)
dim_date["day"] = dim_date["Date"].dt.day
```

### 3. Load

The transformed DataFrames are loaded into MySQL using SQLAlchemy and PyMySQL.

```python
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://USER:PASSWORD@localhost:3306/etl_project"
)
```

Pandas `to_sql()` is then used to load the tables into the database.

```python
dim_store.to_sql(
    "dim_store",
    engine,
    if_exists="replace",
    index=False
)
```

The pipeline creates the following MySQL tables:

```text
etl_project
│
├── dim_store
├── dim_date
├── dim_feature
└── fact_sales
```

## SQL Analysis

After loading the transformed data into MySQL, SQL queries can be used to analyze retail sales.

### Total Sales by Store Type

```sql
SELECT
    ds.type,
    SUM(fs.weekly_sales) AS total_sales
FROM dim_store AS ds
LEFT JOIN fact_sales AS fs
    ON ds.store = fs.store
GROUP BY ds.type;
```

### Total Sales by Department

```sql
SELECT
    dept,
    SUM(weekly_sales) AS total_sales
FROM fact_sales
GROUP BY dept
ORDER BY total_sales DESC;
```

### Top 10 Stores by Sales

```sql
SELECT
    store,
    SUM(weekly_sales) AS total_sales
FROM fact_sales
GROUP BY store
ORDER BY total_sales DESC
LIMIT 10;
```

### Sales by Year

```sql
SELECT
    dd.year,
    SUM(fs.weekly_sales) AS total_sales
FROM fact_sales AS fs
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.year
ORDER BY dd.year;
```

### Holiday vs Non-Holiday Sales

```sql
SELECT
    dd.isholiday,
    AVG(fs.weekly_sales) AS avg_weekly_sales
FROM fact_sales AS fs
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.isholiday;
```

Additional analytical queries are available in the `query/` directory.

## Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd retail_sales_ETL_pipeline
```

### 2. Install Dependencies


The main dependencies are:

```text
pandas
sqlalchemy
pymysql
```

### 3. Create the MySQL database

Connect to MySQL and create the database:

```sql
CREATE DATABASE etl_project;
```

### 4. Configure database credentials

Configure your local MySQL connection with:

```text
DB_HOST=localhost
DB_PORT=3306
DB_NAME=etl_project
DB_USER=<your_mysql_user>
DB_PASSWORD=<your_mysql_password>
```

Database credentials should not be committed to the repository.

### 5. Run the ETL pipeline

```bash
python main.py
```

A successful execution will extract the source data, transform it, create the required tables, and load the results into MySQL.

## Example Output

After running the pipeline, verify the tables in MySQL:

```sql
USE etl_project;

SHOW TABLES;
```

Then query the loaded data:

```sql
SELECT * FROM dim_store LIMIT 5;
SELECT * FROM dim_date LIMIT 5;
SELECT * FROM dim_feature LIMIT 5;
SELECT * FROM fact_sales LIMIT 5;
```

## Skills Demonstrated

This project demonstrates:

- Building an end-to-end ETL pipeline
- Data extraction using Pandas
- Data cleaning and transformation
- Working with dates and time-based attributes
- Fact and dimension table modeling
- Connecting Python to MySQL
- Loading DataFrames into a relational database
- SQL joins and aggregations
- Analytical SQL queries
- Structuring a Python data engineering project

## Author

Built as a data engineering portfolio project to practice ETL development, dimensional data modeling, MySQL, and analytical SQL.
