from datetime import datetime
from typing import Any, Dict, List

from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context
from internal.resources.hooks.json_file import JSONFileHook
from internal.resources.hooks.tabnews import TabNewsHook


class TabNewsEndpointNotFound(Exception):
    ...


class TabNewsToJSONFileOperator(BaseOperator):
    def __init__(
        self,
        tabnews_conn_id: str,
        endpoint: str,
        root_directory: str,
        *args,
        **kwargs,
    ):
        self.__endpoint = endpoint
        self.__tabnews_hook = TabNewsHook(tabnews_conn_id)
        self.__root_directory = root_directory
        super().__init__(*args, **kwargs)

    def write(self, content: List[Dict]):
        json_hook = JSONFileHook(self.__root_directory)
        date = datetime(year=2023, month=8, day=3)
        year = date.year
        month = date.month
        day = date.day

        filename = f"year={year}/month={month}/day={day}/{year}{month}{day}.json"
        json_hook.save(content, filename)

    def execute(self, context: Context) -> Any:
        # algum comportamento

        if not self.__endpoint:
            raise TabNewsEndpointNotFound("Endpoint is required.")

        contents = self.__tabnews_hook.get_rows(endpoint=self.__endpoint)
        self.log.info(f"{len(contents)} registros foram recuperados.\n")

        self.write(content=contents)
