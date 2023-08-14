import json
from os.path import join, dirname, exists
from pathlib import Path
from typing import Dict, List

from airflow.hooks.base import BaseHook


class JSONFileHook(BaseHook):
    def __init__(self, root_directory: str):
        self.__root = root_directory

    def save(self, content: List[Dict], filename: str):
        root_path = join(self.__root, filename)

        repo = dirname(root_path)

        if not exists(repo):
            Path(repo).mkdir(parents=True, exist_ok=True)

        with open(root_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(content, ensure_ascii=False, indent=2))
            file.write("\n")
            self.log.info(f"File has been saved at `{root_path}`")
