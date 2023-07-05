# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuPipeline:
    def __init__(self):
        dbparams = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'database':'Jianshu',
            'charset':'utf-8'

        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self._sql,(item['title'], item['content']))
        self.conn.commit()
        return item


    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into Jianshu(title, content) values(%s, %s)
            """
            return self._sql
        return self._sql


