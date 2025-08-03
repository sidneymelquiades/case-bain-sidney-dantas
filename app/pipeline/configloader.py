import yaml
import os

def load_config(path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+'/config/config.yaml'):
    
    return yaml.safe_load(open(path, 'r'))