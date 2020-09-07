import pandas as pd
import matplotlib.pyplot as plt
clusters = pd.read_csv("ClusterPlot.csv")

from sklearn.cluster import KMeans

x=clusters.copy()
kmeans=KMeans(n_clusters=3,random_state=0)
kmeans.fit(x)
kmeans.predict(x)
result=x.copy()
result['result_pred']=kmeans.fit_predict(x)

plt.scatter(clusters['V1'],clusters['V2'],c=result['result_pred'])
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()