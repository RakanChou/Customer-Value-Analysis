#-*- coding: utf-8 -*-
#数据清洗，过滤掉不符合规则的数据

import pandas as pd
import numpy as np
import datetime

datafile='C:/Users/pc/Desktop/数据挖掘课程设计/tmp/data_cleaned.xls'
data=pd.read_excel(datafile)
d1, d2 = [], []
for x in data['LOAD_TIME']:
    d1.append(datetime.datetime.strptime(x, '%Y/%m/%d'))
for y in data['FFP_DATE']:
    d2.append(datetime.datetime.strptime(y, '%Y/%m/%d'))

d3 = [d1[i] - d2[i] for i in range(len(d1))]
data['L'] = [round((x.days / 30), 2) for x in d3]
data2 = data[['L', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
data2.columns = ['L', 'R', 'F', 'M', 'C']
data2.to_csv('C:/Users/pc/Desktop/数据挖掘课程设计//data/zscoredata1.csv',  index=False)