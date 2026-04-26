def normalize_column_names(df):
    for col in df.columns:
        df = df.withColumnRenamed(col, col.lower())
    return df
