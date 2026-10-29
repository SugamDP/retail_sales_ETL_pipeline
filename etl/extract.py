#import pandas module
import pandas as pd

def extract_data():

    #read the csv files

    features_df = pd.read_csv(r"C:\datascience_oct_26\etl_project\csv_files\Features_dataset.csv")
    sales_df = pd.read_csv(r"C:\datascience_oct_26\etl_project\csv_files\sales_dataset.csv")
    stores_df = pd.read_csv(r"C:\datascience_oct_26\etl_project\csv_files\stores_dataset.csv")

    print('Features Dataset')
    print(features_df.head())
    print(features_df.dtypes)

    print('Sales Dataset')
    print(sales_df.head())
    print(sales_df.dtypes)

    print('Stores Dataset')
    print(stores_df.head())
    print(stores_df.dtypes)

    return features_df, sales_df, stores_df

