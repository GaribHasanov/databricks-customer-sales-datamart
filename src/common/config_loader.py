import yaml
import os


def load_config(env: str):
    base_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

    config_path = os.path.join(base_path, f"config/{env}.yml")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
