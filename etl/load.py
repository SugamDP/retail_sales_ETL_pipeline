import pandas as pd
from sqlalchemy import create_engine

def load_data(fact_sales, dim_store, dim_date, dim_feature):

    db_name = "etl_project"
    db_host = "localhost"
    db_port = 3306
    db_pass = "#######"
    db_user = "root"

    engine = create_engine(
        f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    )

    dim_store.to_sql('dim_store', 
                     engine, 
                     if_exists = 'replace', 
                     index = False)
    dim_date.to_sql('dim_date', 
                         engine, 
                         if_exists = 'replace', 
                         index = False)
    dim_feature.to_sql('dim_feature', 
                         engine, 
                         if_exists = 'replace', 
                         index = False)
    fact_sales.to_sql('fact_sales', 
                         engine, 
                         if_exists = 'replace', 
                         index = False)

    print("Data loaded to MySQL successfully!")