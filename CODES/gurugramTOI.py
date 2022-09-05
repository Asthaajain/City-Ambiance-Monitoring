from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import datetime

format_data = "%Y-%m-%d %H:%M:%S"



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
            self.insertData(a.find('title').text,a.find('pubdate').text,a.link.next_sibling.replace('\n','').replace('\t',''),a.find('description').text,'TimesOfIndia')

        self.conn.close()

    def insertData(self,title,date,url,description, source):
    
        s = date
        x = "T"
        y = " "
        table = s.maketrans(x, y)

        date=s.translate(table)
        print("\n")
        
        mydate = datetime.strptime(date[0:-6], format_data)  
        #print(mydate)
        myCursor= self.conn.cursor()

        
        query = "INSERT INTO `gurugram`(`title`,`date`,`url`, `description`, `source`) VALUES(%s,%s,%s,%s,%s)"

        print(type(mydate))
        thisdate = "%s"%(mydate)
        start_index = description.rindex("</a>")
        args=(title,thisdate,url,description[start_index+4:],source)
        myCursor.execute(query,args)
        self.conn.commit()
 
if __name__ == '__main__':
 
    feed = ReadRss('https://timesofindia.indiatimes.com/rssfeeds/6547154.cms', headers)
    #print(feed.title)
    #print(feed.urls)
    #print(feed.pub_dates)
    #print(feed.descriptions)
