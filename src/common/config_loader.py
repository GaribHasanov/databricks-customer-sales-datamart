import yaml

def load_config(env: str):
    path = f"configs/{env}.yaml"

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    return config
