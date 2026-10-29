from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    print('Pipeline Started')

    #Run the ETL Pipeline

    features_df, sales_df, store_df = extract_data()
    fact_sales, dim_store, dim_date, dim_feature = transform_data(features_df, sales_df, store_df)
    load_data(fact_sales, dim_store, dim_date, dim_feature)

    print('Pipeline completed! Data loaded to MySQL successfully')


if __name__ == "__main__":
    run_pipeline()