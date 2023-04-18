#-*- coding: utf-8 -*- 
#对数据进行基本的探索
#返回最大最小值

import pandas as pd

datafile= 'C:/Users/pc/Desktop/数据挖掘课程设计/data/zscoredata1.csv' #航空原始数据,第一行为属性标签
resultfile1 = 'C:/Users/pc/Desktop/数据挖掘课程设计/tmp/explore2.xls' #数据探索结果表

data = pd.read_csv(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

explore = data.describe(percentiles = [], include = 'all').T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
explore = explore[[ 'max', 'min', 'mean', 'std']]
explore.columns = [ u'最大值', u'最小值', u'平均值', u'方差'] #表头重命名
explore.to_excel(resultfile1) #导出结果