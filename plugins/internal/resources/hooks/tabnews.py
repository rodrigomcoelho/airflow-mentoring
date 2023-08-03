import json
from time import sleep
from typing import Dict, List

from airflow.hooks.base import BaseHook
from requests import HTTPError, get


class TabNewsHook(BaseHook):
    def __init__(self, context=None):
        super().__init__(context)
        self.__base_url = "https://www.tabnews.com.br/api/v1"

    def fetch_api(self, endpoint: str) -> List[Dict]:
        url = self.__base_url + endpoint

        retries = 3

        while retries > 0:
            try:
                response = get(url=url)
                response.raise_for_status()
            except HTTPError as error:
                self.log.error(error)
                sleep((4 - retries) * 60)
                retries -= 1  # retries = retries - 1

            else:
                return json.loads(response.content)

        raise ValueError("Could not reach to the API")

    def get_content(self) -> List[Dict]:
        contents = self.fetch_api("/contents")

        return contents
