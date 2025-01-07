import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Estatísticas do dataset:")
print(data.describe())

kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(data)

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data.iloc[:, :-1])
data['PCA1'] = data_pca[:, 0]
data['PCA2'] = data_pca[:, 1]

plt.figure(figsize=(8,6))
sns.scatterplot(
    x='PCA1', y='PCA2', hue='Cluster', data=data, palette='Set1', s=100
)
plt.title("Cluster no Dataset Iris")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.legend(title="Cluster")
plt.show()

print("Centróides dos clusters:")
print(kmeans.cluster_centers_)


from sklearn.metrics import silhouette_score
score = silhouette_score(data.iloc[:, :-1], data['Cluster'])
print(f"Coeficiente de Silhueta: {score:.2f}")