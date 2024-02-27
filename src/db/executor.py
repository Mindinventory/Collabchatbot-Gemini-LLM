from config.dev import DatabaseSettings as conf
import mysql.connector
import sqlite3
import pandas as pd


class DatabaseExecutor:
    def __init__(self) -> None:
        self.mysql_connection = mysql.connector.connect(
            host=conf.DATABASE_HOST,
            user=conf.DATABASE_USERNAME,
            password=conf.DATABASE_PASSWORD,
            database=conf.DATABASE_NAME,
        )
        self.cur = self.mysql_connection.cursor()

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            data = self.cur.fetchall()
            columns = [desc[0] for desc in self.cur.description]
            return data, columns
        except Exception as error:
            print(error)
        finally:
            self.cur.close()
            self.mysql_connection.close()

    def execute_only(self, query):
        try:
            self.cur.execute(query)
        except Exception as error:
            print(error)
        finally:
            self.cur.close()
            self.mysql_connection.close()


class SqliteDbExecutor:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(conf.SQLITE_URL)

    def execute_query(self, query):
        try:
            result = pd.read_sql_query(query, self.connection)
            return result
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
            return pd.DataFrame()
        finally:
            self.connection.close()

    def execute_only(self, query):
        try:
            result = pd.read_sql_query(query, self.connection)
            return result
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
            return pd.DataFrame()
        finally:
            self.connection.close()
