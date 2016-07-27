# weibospider
    This spider can download all gif images of specific users of sinaweibo.
    gif images stored in mysql, and gif sotred in D:/spiders/weibo/gaoxiao. You can change the location.
    
    3 steps needed:
    
    1.create mysql db.
      +-------------+------------------+------+-----+---------+----------------+
      | Field       | Type             | Null | Key | Default | Extra          |
      +-------------+------------------+------+-----+---------+----------------+
      | id          | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
      | url         | varchar(80)      | NO   | UNI | NULL    |                |
      | name        | varchar(50)      | NO   | UNI | NULL    |                |
      | description | varchar(500)     | YES  |     | NULL    |                |
      | blogger     | varchar(20)      | NO   |     | NULL    |                |
      | bloggerid   | varchar(20)      | NO   |     | NULL    |                |
      +-------------+------------------+------+-----+---------+----------------+
      name is the name of gif file which will be downloaded.
      
    2.crawl gif information.
      cmd:scrapy crawl wb
      
    3.download gif img.
      cmd:scrapy crawl gif
