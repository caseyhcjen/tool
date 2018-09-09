import abc
import pyodbc
import pandas as pd
import urllib
import sqlalchemy
import os
import abc
import cx_Oracle

import numpy as np
from datetime import datetime

class DB(object):
    def __init__(self, database=None):
        self.connection = self.get_connection(database)

    @abc.abstractmethod
    def get_connection(self):
        """Get connection"""

    @abc.abstractmethod
    def getEngine(self):
        """Get getEngine"""

    def sql_to_df(self, sqlStr=None):
        df = pd.read_sql(sql=sqlStr, con=self.connection)
        return df


class Oracle(DB):
    def get_connection(self, database=None):
        # print "Using Oracle."
        '''
         #e.g. test on Oracle Server
        '''
        #print "Getting Oracle database."
        conn_str = os.environ[database]
        # print conn_str
        return cx_Oracle.connect(conn_str)


    def getEngine(self,connStr):
        return sqlalchemy.create_engine("oracle+cx_oracle://" + connStr)


class MSSql(DB):
    def get_connection(self, database=None):
        ConnStr = os.environ[database]
        return pyodbc.connect(ConnStr, autocommit=True)


    def getEngine(self, connStr):
        params = urllib.quote_plus(connStr)
        engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        return engine

