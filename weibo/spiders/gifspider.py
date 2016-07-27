import scrapy
from . import mysql
from . import const
import time
import os

class GifSpider(scrapy.Spider):
	name = 'gif'
	allowed_domains = const.ALLOW_DOMAINS
	headers = const.HEADERS

	def parse(self,response):
		os.chdir('D://spiders/weibo/gaoxiao')
		print('该网页是图片')
		filename = response.url.split('/')[-1]
		with open(filename, 'wb') as f:
			f.write(response.body)

	def start_requests(self):
		self.db = mysql.MySQL(const.DB_CONFIG['host'],const.DB_CONFIG['user'],const.DB_CONFIG['passwd'],const.DB_CONFIG['db'],const.DB_CONFIG['port'],const.DB_CONFIG['charset'],const.DB_CONFIG['timeout'])
		urls = self.db.query('select url from gaoxiao')
		for url in urls:
			time.sleep(3)
			yield scrapy.Request(url[0],callback=self.parse)			
