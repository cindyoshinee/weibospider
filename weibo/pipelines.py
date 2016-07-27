# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from weibo.spiders import const
import pymysql

class WeiboPipeline(object):
	def __init__(self):
		print('connect...')
		self.conn = pymysql.connect(host=const.DB_CONFIG['host'], user=const.DB_CONFIG['user'], passwd=const.DB_CONFIG['passwd'], db=const.DB_CONFIG['db'], port=const.DB_CONFIG['port'], charset=const.DB_CONFIG['charset'], connect_timeout=const.DB_CONFIG['timeout'])
		self.cursor = self.conn.cursor()
	def process_item(self, item, spider):
		sql = 'insert into gaoxiao(url,name,description,blogger,bloggerid) values ("%s","%s","%s","%s","%s")' % (item['url'],item['name'],item['description'],item['blogger'],item['bloggerid'])
		self.cursor.execute(sql)
		self.conn.commit()
		print('存数据..')
		return item
	def  open_spider(self,spider):
		pass
	def close_spider(self,spider):
		self.cursor.close()
		self.conn.close()