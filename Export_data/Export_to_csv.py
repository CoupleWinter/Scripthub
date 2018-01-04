# coding:utf-8

import pandas as pd
from sqlalchemy import MetaData, Table, create_engine


class AssetExpiry(object):
    def __init__(self):
        self.host = ''
        self.port = ''
        self.user = ''
        self.password = ''
        self.database = ''
        self.charset = ''

    def fun(self):
        engine = create_engine('mysql+pymysql://{username}:{pwd}@{host}/{database}'.format(username=self.user,
                                                                                           pwd=self.password,
                                                                                           host=self.host,
                                                                                           database=self.database))
        conn = engine.connect()
        metadata = MetaData(conn)
        tbl = Table('table_name', metadata, autoload=True, schema=self.database)
        sql = tbl.select()
        result = conn.execute(sql)
        df = pd.DataFrame(data=list(result), columns=result.keys())
        name_csv = 'table.csv'
        name_text = 'table.txt'
        # index 导出列名
        df.to_csv(name_csv, index=True)
        conn.close()


if __name__ == '__main__':
    AssetExpiry().fun()
