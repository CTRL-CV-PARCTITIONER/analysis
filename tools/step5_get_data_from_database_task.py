import os
import sys
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
import argparse
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))
from typing import Any, Union
import pandas as pd
import random
from configuration.config import _sqlParam, Fore_colors, reset_color
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.engine.base import Connection, Engine

_len = len(Fore_colors)

class ConnectDdatabase(object):
    def __init__(self, param) -> Any:
        self.username: str = param["username"]
        self.password: str = param["password"]
        self.host: str = param["host"]
        self.port: str = param["port"]
        self.database: str = param["database"]
        self.mode: str = param["mode"]
        self.engine: Engine = self.connect_database()
        self.table: Any = param["table"]
        self.save: str = param["save"]
        self.show()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def random_color(self, word: str):
        randomInt = random.randint(0, _len - 1)
        Fore_color = Fore_colors[randomInt]
        return Fore_color + word + reset_color
    
    def connect_database(self) -> Engine:
        engine = create_engine(
            f'mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'
        )
        inspector = inspect(engine).default_schema_name
        logger.info (self.random_color(f"{inspector} Successfully connected to the database"))
        return engine

    def write_to_database(self, data: pd.DataFrame) -> Any:
        try:
            ret = data.to_sql(name=self.table, con=self.engine, if_exists=self.mode, index=False)
            return ret
        except Exception as e:
            logger.error (self.random_color(e))
            return
        finally:
            logger.info (self.random_color(f"Write successfully to {self.database} - {self.table}"))

    def read_from_database(self, sql: str) -> tuple:
        conn = self.engine.connect()
        result = conn.execute(text(sql))
        columns = list(result.keys())
        return (columns, result.fetchall())
    
    def generate_dataframe(self, columns: list, value: Union[list, dict]) -> pd.DataFrame:
        dataframe = pd.DataFrame(
            data=value,
            columns=columns,
        )
        return dataframe
    
    def save_local(self, data: pd.DataFrame) -> Any:
        file_type = self.save.split("/")[-1].split(".")[-1]
        try:
            if file_type in ["xlsx", "xls"]: data.to_excel(self.save, index=False)
            if file_type in ["csv"]: data.to_csv(self.save, index=False)
        except Exception as e:
            logger.error (self.random_color(e))
            return
        finally:
            logger.info (self.random_color(f"Successfully generate {self.save}"))
    
    def close_connect(self) -> Any:
        inspector = inspect(self.engine).default_schema_name
        self.engine.connect().close()
        logger.info (self.random_color(f"{inspector} The connection to the database '{self.database}' has been closed. Procedure"))
    
    def show(self) -> Any:
        get_tables = [tuple_table[0] for tuple_table in list(self.read_from_database("show tables")[1:])[0]]
        logger.info (
            self.random_color(f"{self.database} tables: {str(get_tables)}")
        )
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate video for current pipline")
    parser.add_argument("--sql", default="select * from student", help="img location original path")
    args = parser.parse_args()
    Connect = ConnectDdatabase(param=_sqlParam)
    columns, value = Connect.read_from_database(sql=args.sql)
    dataframe = Connect.generate_dataframe(columns=columns, value=value)
    Connect.save_local(dataframe)
    Connect.write_to_database(dataframe)
    Connect.close_connect()