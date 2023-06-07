# -*- coding: utf-8 -*-
import requests
import pandas as pd
url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
rows = []
for i in range(1,5):
    params = {'bondType': '100001', 'issueYear': '2023', 'pageNo': str(i),'pageSize': '15'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.post(url, params=params,headers=headers)
    data = response.json()
    # 解析返回的表格数据
    table_data = data["data"]["resultList"]
    #print(len(table_data))
    columns = ["isin","bondCode","entyFullName","bondType","issueStartDate","debtRtng"]

    for record in table_data:
        row = [record[col] for col in columns]
        rows.append(row)
new_colum = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]

df = pd.DataFrame(rows, columns=new_colum)
df.to_csv("bond_data.csv", index=False)
