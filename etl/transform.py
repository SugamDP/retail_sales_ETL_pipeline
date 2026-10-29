import pandas as pd

def transform_data(features_df, sales_df, stores_df):

    #transform the data type (wrongly handled by numpy)
    features_df['Date'] = pd.to_datetime(features_df['Date'])
    sales_df['Date'] = pd.to_datetime(sales_df['Date'], dayfirst=True)

    #create the stores dimension table
    dim_store = stores_df.drop_duplicates().reset_index(drop = True)

    #create the sales dimension table
    #just extract the Date and IsHoliday attributes
    dim_date = sales_df[['Date', 'IsHoliday']].drop_duplicates().copy()

    #further extract the year, month, and week
    dim_date['year'] = dim_date['Date'].dt.year
    dim_date['month'] = dim_date['Date'].dt.month
    dim_date['week'] = dim_date['Date'].dt.isocalendar().week.astype(int)

    #create the feature dimension table
    #to drop the unwanted columns
    markdown_colums = ["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"]
    features_df = features_df.drop(columns = markdown_colums, errors = 'ignore')

    dim_feature = features_df.drop_duplicates().reset_index(drop = True)


    #create fact sales table
    fact_sales = sales_df.copy()

    def normalize(df):
        #convert the columns into
        df.columns = df.columns = df.columns.str.lower().replace("", "_")
        return df


    #call the normalize method on the dimension tables  and fact table

    dim_date = normalize(dim_date)
    dim_feature = normalize(dim_feature)
    dim_store = normalize(dim_store)
    fact_sales = normalize(fact_sales)

    return fact_sales, dim_store, dim_date, dim_feature


