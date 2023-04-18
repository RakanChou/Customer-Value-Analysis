import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
inputfile = 'C:/Users/pc/Desktop/数据挖掘课程设计/tmp/zscoreddata1.xls' #待聚类的数据文件
resultfile = 'C:/Users/pc/Desktop/数据挖掘课程设计/tmp/kmeans.csv'
k = 5                       #需要进行的聚类类别数

#读取数据并进行聚类分析
data = pd.read_excel(inputfile) #读取数据

#调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型
r1 = pd.Series(kmodel.labels_).value_counts()
r2 = pd.DataFrame(kmodel.cluster_centers_)
r3 = pd.Series(['客户群1', '客户群2', '客户群3', '客户群4', '客户群5', ])
r = pd.concat([r3, r1, r2], axis=1)

r.columns = ['聚类类别', '聚类个数'] + list(data.columns)
r.to_csv(resultfile , encoding='utf_8_sig', index=False)