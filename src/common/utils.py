for col in df.columns:
    df = df.withColumnRenamed(col, col.lower())
