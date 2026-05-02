import os
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat

w = WorkspaceClient(
    host=os.environ["DATABRICKS_HOST"],
    token=os.environ["DATABRICKS_TOKEN"]
)

with open("notebooks/01_bronze_customer_ingestion.py", "rb") as f:
    content = f.read()

w.workspace.import_(
    path="/Users/bronze/01_bronze_customer_ingestion",
    format=ImportFormat.SOURCE,
    content=content,
    overwrite=True
)

print("DEPLOY SUCCESS")
