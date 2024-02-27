from ..executor import DatabaseExecutor, SqliteDbExecutor
from .. import queries
import pandas as pd
import os
from utils import constants


def cache_all():
    # DatabaseExecutor().execute_only(
    #     "SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")  # This is a temporary fix. To be removed later.
    #
    cache(constants.EMPLOYEE_PROFILE, queries.EMPLOYEE_PROFILE)
    cache(constants.TEAM_INFO, queries.TEAM_INFO)
    cache(constants.AGENDA_MANAGEMENT, queries.AGENDA_MANAGEMENT)


def get_df(query: str):
    # data, columns = DatabaseExecutor().execute_query(query)
    # return pd.DataFrame(data, columns=columns)
    return SqliteDbExecutor().execute_query(query)


def cache(path: str, query: str):
    if not os.path.exists(path):
        os.makedirs(path)
    clear_file(path)
    data = get_df(query)
    data.to_pickle(path)


def clear_file(path):
    try:
        with open(path, "w") as f:
            pass
    except FileNotFoundError:
        print(f"File not found at {path}")


def get_df_from_cache(path) -> pd.DataFrame:
    try:
        return pd.read_pickle(path)
    except Exception:
        print(f"Could not load cache from {path}")
