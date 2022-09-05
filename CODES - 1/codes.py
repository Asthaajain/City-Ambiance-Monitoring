import schedule
import time
import os
def hello():
    os.system('bengaluruNIE.py')
    os.system('bengaluruTH.py')
    os.system('bengaluruTOI.py')
    os.system('bengaluruHT.py')

    os.system('delhiHT.py')
    os.system('delhiNIE.py')
    os.system('delhiTH.py')
    os.system('delhiTOI.py')

    os.system('chandigarhHT.py')
    os.system('chandigarhTIE.py')
    os.system('chandigarhTOI.py')

    os.system('gurugramHT.py')
    os.system('gurugramTOI.py')

    os.system('hyderabadNIE.py')
    os.system('hyderabadTH.py')
    os.system('hyderabadTOI.py')

    os.system('kolkataHT.py')
    os.system('kolkataNIE.py')
    os.system('kolkataTH.py')
    os.system('kolkataTOI.py')

    os.system('mumbaiHT.py')
    os.system('mumbaiNIE.py')
    os.system('mumbaiTH.py')
    os.system('mumbaiTOI.py')

    os.system('puneHT.py')
    os.system('puneTOI.py')

    
schedule.every(30).seconds.do(hello)

while(1):
    schedule.run_pending()
    time.sleep(1)
