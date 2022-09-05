from bs4 import BeautifulSoup
import requests
import pymysql
 
headers = {
            'User-Agent': 'your-user-agent-here'
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
        #self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        #self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        
        #self.descriptions = [d['description'] for d in self.articles_dicts if 'description' in d]

        #self.pub_dates = [d['pubdate'] for d in self.articles_dicts if 'pubdate' in d]
        self.conn.close()

    def insertData(self,title,date,url,description, source):
        myCursor= self.conn.cursor()
        query = "INSERT INTO `delhi`(`title`, `url`, `description`, `source`) VALUES(%s,%s,%s,%s)"
        args=(title,url,description,source)
        myCursor.execute(query,args)
        self.conn.commit()
        
        


        
if __name__ == '__main__':
 
    feed = ReadRss('https://www.thehindu.com/news/cities/Delhi/feeder/default.rss', headers)
    print(feed.titles)
    print(feed.urls)
    print(feed.pub_dates)
    print(feed.descriptions)
