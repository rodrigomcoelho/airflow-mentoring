from typing import Any
from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context
from internal.resources.hooks.tabnews import TabNewsHook

class TabNewsOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__tabnews_hook = TabNewsHook(None)

    def execute(self, context: Context) -> Any:
        # algum comportamento

        contents = self.__tabnews_hook.get_content()
        self.log.info(f"{len(contents)} registros foram recuperados.\n")

        for content in contents:
            self.log.info(content)
