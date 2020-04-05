from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

while True:
    def notifyMe(title,message):
        notification.notify(
                title=title,
                message=message,
                app_icon = "C:\\Users\\HAPPY\\Desktop\\Projects\\icon.ico",
                timeout=4
            )
    def getData(url):
        r=requests.get(url)
        return r.text


    if __name__ == "__main__":
        
        myHtmlData=getData('https://www.mohfw.gov.in/')
        
        soup = BeautifulSoup(myHtmlData, 'html.parser')

        mystr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mystr += tr.get_text()
        mystr=mystr[1:]
        itemlist=mystr.split("\n\n")
        states=['Maharashtra','Uttar Pradesh']
        total=['Total number of confirmed cases in India']
        for item in itemlist[0:31]:
            dataList=item.split("\n")
            if dataList[1] in states:
                nTitle="Live Corona Status..."
                nText=f"State : {dataList[1]}\nConfirmed : {dataList[2]}\nCured/Migrated : {dataList[3]}\nDeaths : {dataList[4]}"
                notifyMe(nTitle, nText)
                time.sleep(4)
                
            if dataList[0]=='Total number of confirmed cases in India':
                print("s1")
                nTitle=f"Total Confirmed Cases in India: {dataList[1]}"
                nText="Wash Hands Now....."
                
                notifyMe(nTitle, nText)
    time.sleep(3600)            
