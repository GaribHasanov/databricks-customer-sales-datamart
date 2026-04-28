import yaml
import os

def load_config(env: str):
    # Bu funksiya avtomatik olaraq layihənin kökünü tapıb config-i oxuyacaq
    # /Workspace/Repos/.../project/src/common -> /Workspace/Repos/.../project/
    current_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
    
    config_path = f"{project_root}/config/{env}.yml"
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config tapılmadı: {config_path}")
        
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
