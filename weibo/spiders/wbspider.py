import scrapy
from . import const
from . import mysql
import os
import json
from weibo.items import WeiboItem
import re
import time

class WbSpider(scrapy.Spider):
	name = 'wb'
	allowed_domains = const.ALLOW_DOMAINS
	headers = const.HEADERS
	start_urls = ['http://ww1.sinaimg.cn/large/8eda1a63jw1f62y54eu7ag206y094nph.gif',]

	#['http://m.weibo.cn/page/json?containerid=1005055064796580_-_WEIBO_SECOND_PROFILE_WEIBO&page=1']

	def parse(self,response):
		print('当前url为：%s' % response.url)
		if '.gif' in response.url: 
			return self.parse_gif(response)
		elif 'page' in response.url:
			return self.parse_page(response)
		else:
			print('跳过该网页')

	def parse_gif(self,response):
		os.chdir('D://spiders/weibo/gaoxiao')
		print('该网页是图片')
		filename = response.url.split('/')[-1]
		with open(filename, 'wb') as f:
			f.write(response.body)

	def parse_page(self,response):
		print('该网页是信息')
		self.text = json.loads(response.body_as_unicode())
		if response.url[-6:] == 'page=1':
			self.max_page = self.text['cards'][0]['maxPage']
		for each in self.text['cards'][0]['card_group']:
			try:
				self.info = each['mblog']['retweeted_status']
			except KeyError:
				self.info = each['mblog']
			self.blogger = self.info['user']['screen_name']
			self.bloggerid = self.info['user']['id']
			self.description = self.info['text']
			try:
				self.pics = each['mblog']['retweeted_status']['pics']
				for eachpic in self.pics:
					self.picurl = eachpic['url']
					if '.gif' in self.picurl:
						while '</i>' in self.description:
							self.html = re.search(r'<i(.*?)</i>',self.description).group()
							self.description = self.description.replace(self.html,'')
							print(self.description)
						if 'thumb180' in self.picurl:
							self.picurl = self.picurl.replace('thumb180','large')
						else:
							self.picurl = self.picurl.replace('wap180','large')
						name = self.picurl.split('/')[-1]
						time.sleep(3)
						yield self.store_item({'url':self.picurl, 'name':name, 'description':self.description, 'blogger':self.blogger, 'bloggerid':self.bloggerid})
			except KeyError:
				pass
		try:
			for i in range(2, self.max_page+1):
				point = response.url.index('page=')
				urli = response.url[:point] + 'page=' + str(i)
				yield scrapy.Request(urli,headers=self.headers, callback=self.parse)
		except AttributeError:
			pass

	def store_item(self,data):
		item = WeiboItem()
		item['url'] = data['url']
		item['name'] = data['name']
		item['description'] = data['description']
		item['blogger'] = data['blogger']
		item['bloggerid'] = data['bloggerid']
		return item
	