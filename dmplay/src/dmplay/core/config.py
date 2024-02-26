import os
import json
import shutil
from typing import List, Optional
from loguru import logger
from pydantic import BaseModel


class Config(BaseModel):

    NICKNAME: Optional[str]
    USERNAME: Optional[str]
    PASSWORD: Optional[str]
    ACCESS_TOKEN: Optional[str]
    REMBER_PASSWORD: Optional[bool]
    LIVE_URL_ID: Optional[str]
    SYS_USER_ID: Optional[int]
    AVATAR_URL: Optional[str]
    DOWNLOAD_PATH: str
    PART_RULE: List[str]


def load_config_from_json():
    config_path = os.path.dirname(os.path.abspath(__file__)) 
    old_path = os.path.join(config_path, "config.json")
    example_config_path = os.path.join(config_path, "config.example.json")
    if not os.path.exists(old_path):
        shutil.copy(
            os.path.join(config_path, "config.example.json"),
            os.path.join(config_path, "config.json"),
        )
    with open(example_config_path, "r", encoding="utf-8") as r:
        example_config = json.load(r)
    with open(old_path, "r", encoding="utf-8") as f:
        old_config = json.load(f)
    for c in example_config:
        if c not in old_config:
            old_config[c] = example_config[c]
    return Config(**old_config)


def save_config_to_json(cfg: Config):
    logger.info(cfg)
    global config
    config_path = os.path.dirname(os.path.abspath(__file__)) 
    old_path = os.path.join(config_path, "config.json")
    with open(old_path, "w", encoding="utf-8") as w:
        json.dump(cfg.model_dump(), w)
    config = cfg


config = load_config_from_json()
    
