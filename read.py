
import pandas as pd


def url_data():
    df = pd.read_excel('output_data.xlsx', )
    data =[]
    index = 2
    for iindex, row in df.iterrows():
        lst = (list(row))
        lst.append(index)
        index +=1
        lst[2] = str(lst[2])
        if lst[2]=='nan':
            res = []
            lst[1] = f'https://{lst[1]}/ads.txt'

            res.append(lst[1])
            res.append(lst[-1])
            
            data.append(res)
    if len(data)== 0 :
        return None
    else:
        return data
        
        





    

