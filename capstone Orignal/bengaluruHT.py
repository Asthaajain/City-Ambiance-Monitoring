from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import datetime

#dt = datetime.datetime.strptime('date', "%d %b %Y %H:%M:%S")
format_data = "%d %b %Y %H:%M:%S"



headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
        }
 
class ReadRss:
 
    def __init__(self, rss_url, headers):
 
        self.url = rss_url
        self.headers = headers
        
        try:
            self.conn=pymysql.connect(host="localhost", user="root", passwd= "", db="my_python")
            self.r = requests.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
            
        except Exception as e:
            print('Error fetching the URL: ', rss_url)
            print(e)
            
        try:    
            self.soup = BeautifulSoup(self.r.text, 'lxml')
            
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
        self.articles = self.soup.findAll('item')

        for a in self.articles:
            self.insertData(a.find('title').text,a.find('pubdate').text,a.link.next_sibling.replace('\n','').replace('\t',''),a.find('description').text,'thehindu')
            
        #self.articles_dicts = [{'title':a.find('title').text,'link':a.link.next_sibling.replace('\n','').replace('\t',''),'description':a.find('description').text,'pubdate':a.find('pubdate').text} for a in self.articles]
        #self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        #self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        #self.descriptions = [d['description'] for d in self.articles_dicts if 'description' in d]
        #self.pub_dates = [d['pubdate'] for d in self.articles_dicts if 'pubdate' in d]

        self.conn.close()

    def insertData(self,title,date,url,description, source):
        mydate = datetime.strptime(date[14:-9], format_data)
  
        #print(mydate)
        myCursor= self.conn.cursor()
        
        query = "INSERT INTO `bangalore`(`title`,`date`,`url`, `description`, `source`) VALUES(%s,%s,%s,%s,%s)"
        #mycursor.execute('INSERT INTO ` bangalore` (`title`,`date`,`url`, `description`, `source`) VALUES(%s,(dt.strftime('%Y-%m-%d %H:%M:%S'),%s,%s,%s)))

       # mycursor.execute('insert into `bangalore`(`title`,`date`,`url`, `description`, `source`) values(%s, %s)', (id, formatted_date))
        print(type(mydate))
        thisdate = "%s"%(mydate)
        args=(title,thisdate,url,description,source)
        myCursor.execute(query,args)
        self.conn.commit()
 
if __name__ == '__main__':
 
    feed = ReadRss('https://www.hindustantimes.com/feeds/rss/cities/bengaluru-news/rssfeed.xml', headers)
    print(feed.titles)
    print(feed.urls)
    print(feed.pub_dates)
    print(feed.descriptions)
