import pandas
import requests
from bs4 import BeautifulSoup

url="https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l=[]
for page in range(0,30,10):
    request = requests.get(url+str(page)+".html")
    c=request.content
    soup=BeautifulSoup(c,"html.parser")
    
    all=soup.find_all("div",{"class":"propertyRow"})
    for info in all:
        d={}
        try:
            d["Address"]=info.find_all("span",{"class":"propAddressCollapse"})[0].text
        except:
            d["Address"]=None
        d["City"]=info.find_all("span",{"class":"propAddressCollapse"})[1].text
        d["Price"]=info.find("h4",{"class":"propPrice"}).text.replace("\n","")

        try:
            d["Area"]=info.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None    
        try:
            d["Beds"]=info.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None
        try:
            d["Full Baths"]=info.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None
        try:
            d["Half Baths"]=info.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for column_group in info.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text
        l.append(d)
    
df=pandas.DataFrame(l)
df.to_csv("Output.csv")
df
