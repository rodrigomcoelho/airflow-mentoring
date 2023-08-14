import json
from time import sleep
from typing import Dict, List, Optional

from airflow.hooks.base import BaseHook
from requests import HTTPError, get


class TabNewsHook(BaseHook):
    def __init__(self, conn_id: str):
        self.__base_url = self.get_connection(conn_id=conn_id).host

    def fetch_api(self, endpoint: str, params: Optional[Dict] = None) -> List[Dict]:
        url = self.__base_url + endpoint

        retries = 3

        while retries > 0:
            try:
                response = get(url=url, params=params or {})
                response.raise_for_status()
                self.log.warning(response.url)
            except HTTPError as error:
                self.log.error(error)
                sleep((4 - retries) * 60)
                retries -= 1  # retries = retries - 1

            else:
                return json.loads(response.content)

        raise ValueError("Could not reach to the API")

    def get_rows(self, endpoint: str) -> List[Dict]:
        page = 1
        has_more = True

        rows = []

        while has_more:
            contents = self.fetch_api(endpoint, params={"page": page})

            if not contents:
                has_more = False
                break

            rows += contents

            page += 1

        return rows
