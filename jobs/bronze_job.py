from src.bronze.ingest_customers import load_customers

def run():
    df = load_customers("path")
    df.show()

if __name__ == "__main__":
    run()
