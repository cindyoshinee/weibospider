import pymysql

class MySQL:
	def __init__(self,host,user,passwd,db,port,charset,timeout):
		print('connect...')
		self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset, connect_timeout=timeout)
		self.cursor = self.conn.cursor()

	def __del__(self):
		print('close connect...')
		self.cursor.close()
		self.conn.close()

	def update(self,sql):
		print('update sql...')
		self.cursor.execute(sql)
		self.conn.commit()

	def query(self,sql):
		print('query sql...')
		self.cursor.execute(sql)
		rows = self.cursor.fetchall()
		return rows

if __name__ == '__main__':
	db = MySQL('127.0.0.1','root','123456','weibo',3306,'utf8',5)	
	rows = db.query('select * from gaoxiao')
	print(rows)