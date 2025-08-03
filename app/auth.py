import yaml
from fastapi import HTTPException


def load_api_keys(path="security/api_keys.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
        return set(entry["key"] for entry in data["api_keys"])

API_KEYS = load_api_keys()

def verify_api_key(key: str):
    if key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Unauthorized")