import os
import base64
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat

w = WorkspaceClient(
    host=os.environ["DATABRICKS_HOST"],
    token=os.environ["DATABRICKS_TOKEN"]
)

# file oxu və base64 et
with open("notebooks/01_bronze_customer_ingestion.py", "rb") as f:
    content = base64.b64encode(f.read()).decode("utf-8")

w.workspace.import_(
    path="/Users/bronze/01_bronze_customer_ingestion",
    format=ImportFormat.SOURCE,
    content=content,   # artıq string-dir
    overwrite=True
)

print("DEPLOY SUCCESS")
