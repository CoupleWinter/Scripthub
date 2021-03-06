#! usr/bin/env python2.7
# coding:utf-8
# author:Aisuko
# 2017-08-30

import csv
import os
import sys
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine

# try:
#     import cx_Oracle
# except ImportError:
#     raise ImportError('请安装cx_Oracle pip install cx_Oracle')


class StandardError(object):
    pass


class AssetExpiry(object):
    __doc__ = '从数据库导出数据'

    def __init__(self):

        # 用户名
        self.username = ''
        # password
        self.password = ''
        self.host = ''
        # oracle实例名
        self.orcl = ''
        self.database = ''

    def fun(self, **kwargs):
        """
        主函数
        :param kwargs:
        :return:
        """
        try:
            self.__connection()
            # sql = 'Sql'
            # self.sql_for_oracle = self.__get_sql(sql=sql)
            # 返回数据集
            # list_of_content = self.__connection()

            # assert (list_of_content is not None)
            # with open('Excel_to_date.csv', 'wb') as f:
            #     spamwriter = csv.writer(f, dialect='excel')
            #     for i in self.yield_list_of_content(list_of_content):
            #         spamwriter.writerow(i)
        except Exception as e:
            print(Exception(e.message))
        except AssertionError as e:
            print(AssertionError(e.message))

    def yield_list_of_content(self, list_of_content):
        for i in list_of_content:
            yield i

    def __connection(self, **kwargs):
        """
        链接Oracle数据库
        :param kwargs:
        :return:
        """
        try:
            # db = cx_Oracle.connect(self.username_for_oracle, self.password_for_oracle, self.orcl_for_oracle)
            # cursor = db.cursor()
            # cursor.execute(self.sql_for_oracle)
            # row = cursor.fetchall()
            engine = create_engine(
                    'oracle://{username}:{pwd}@{host}/{database}'.format(username=self.username,
                                                                         pwd=self.password,
                                                                         host=self.host,
                                                                         database=self.orcl))
            conn = engine.connect()
            metadada = MetaData(conn)
            tabl = Table('table_name', metadada, autoload=True, schema=self.database)
            sql = tabl.select()
            result = conn.execute(sql)
            df = pd.DataFrame(data=list(result), columns=result.keys())
        except Exception as e:
            raise Exception(e.message)
        else:
            df.to_csv('name.csv', index=True)
            conn.close()

    def __get_sql(self, **kwargs):
        """
        本地获取sql文件
        :param kwargs:
        :return:
        """
        path = os.path.join(sys.path.__getitem__(0), 'get_sql')
        try:
            assert (kwargs.get('sql') is not None)

            if os.path.exists(path):
                with open(os.path.join(path, kwargs.get('sql')), 'rb') as f:
                    t = f.read()
            else:
                raise StandardError('路径下不存在文件，请先创建get_sql文件夹，并把sql文件命名为Sql，放在文件夹根目录')
        except AssertionError as e:
            raise AssertionError(e.message + "please input sql'name")
        except Exception as e:
            raise Exception(e.message)
        else:
            return t
        finally:
            f.close()


if __name__ == '__main__':
    AssetExpiry().fun()
