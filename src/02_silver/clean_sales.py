from pyspark.sql.functions import col

def clean_sales(df):
    return df.dropna().dropDuplicates()
