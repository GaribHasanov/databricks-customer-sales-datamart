from databricks.bundles import job, task

@job(name="bronze_customer_job")
def bronze_customer_job():

    @task
    def load_customer_bronze():
        return {
            "notebook_path": "../notebooks/01_bronze_customer_ingestion.py"
        }
