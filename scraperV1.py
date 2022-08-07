import requests
#import fake_useragent
from bs4 import BeautifulSoup
from read_file import url_data
import csv
from requests.exceptions import Timeout
from requests.exceptions import  ConnectionError
from tqdm import tqdm



DATA = url_data()

def checker(url_input):
    try:
        url = url_input
        
        #user = fake_useragent.FakeUserAgent().random
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        response = requests.get(url,headers = header,timeout=5)
        res_code = response.status_code
        html1 = response.text
        html = html1.replace('\r','\n')
        html_string = html.replace('\r','')
        html_string = html.replace('\n','')
        
        str_data = html_string
        
        lst = html1.replace('\r','').split('\n')
        list_data = [i for i in lst if i ]
        # 403 Error
        if res_code == 404:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = str(res_code)
            result = [r2,r1,r3]
            return result
        #404 Error
        elif response.status_code == 403:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = str(res_code)
            result = [r2,r1,r3]
            return result
        
        #Ezoic
        elif 'ezoic.ai' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Ezoic'
            result = [r2,r1,r3]  
            return result
        
        #adthrive
        elif 'adthrive' in str_data or 'AdThrive' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Adthrive'
            result = [r2,r1,r3] 
            return result
        
        #MONUMETRIC  
        elif 'MONUMETRIC' in str_data or 'monumetric' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Monumetric'
            result = [r2,r1,r3]
            return result
        
        #Mediavine  
        elif 'mediavine.com' in str_data or 'Mediavine' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Mediavine'
            result = [r2,r1,r3]
            return result
        
        #Shemedia
        elif 'shemedia.com' in str_data or 'SHE Media' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Shemedia'
            result = [r2,r1,r3]
            return result

        #Gourmetads
        elif 'gourmetads.com' in str_data or 'GOURMET ADS' in str_data:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Gourmetads'
            result = [r2,r1,r3]
            return result


        #Medianet
        elif ('media.net' in list_data[0] or 'media.net' in list_data[1] or 'media.net' in list_data[2] or 'media.net' in list_data[3]) :
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Medianet'
            result = [r2,r1,r3]
            return result
        elif 'Media.net' in list_data[0] or 'Media.net' in list_data[1] or 'Media.net' in list_data[2] or 'Media.net' in list_data[3]:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Medianet'
            result = [r2,r1,r3]
            return result
        


        #Sovrn
        elif 'sovrn.com' == str_data[0:9]:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Sovrn'
            result = [r2,r1,r3]
            return result


        #Adsense
        elif (len(list_data) == 1 or len(list_data) == 2 or len(list_data) == 3 or len(list_data) == 4 or len(list_data) == 5 or len(list_data) == 6) and ('google.com' in list_data[0] or 'google.com' in list_data[-1]):
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Adsense'
            result = [r2,r1,r3]
            return result         
        elif len(list_data) == 4 and 'google.com' in list_data[3]:
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Adsense'
            result = [r2,r1,r3]
            return result  
        
        
        else:#unknown
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Unknown'
            result = [r2,r1,r3]
            return result      
    
    
    except Timeout:#404
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 404
            result = [r2,r1,r3]
            return result    
    except:#unknown
            r1 = url
            r2 = url.replace('https://www.','').replace('/ads.txt','')
            r3 = 'Unknown'
            result = [r2,r1,r3]
            return result    


    

def get_full_data():
    data_result_list = []

    for url in tqdm(DATA):
        res = checker(url)
        data_result_list.append(res)
    return data_result_list

#print(checker('https://multiply.info/ads.txt'))

