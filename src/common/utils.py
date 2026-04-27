from pyspark.sql import functions as F


def normalize_column_names(df):
    return df.toDF(*[c.lower() for c in df.columns])
