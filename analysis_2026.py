import yfinance as yf
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# --- 2026: The Steel Framework (14 Selected Entities) ---
# 証券コードに日本郵船(9101.T)を含む14銘柄
tickers = [
    '9983.T', '8035.T', '6758.T', '9984.T', '4502.T', 
    '8306.T', '8316.T', '8411.T', '8001.T', '8031.T', 
    '8058.T', '7203.T', '7267.T', '9101.T'
]

print("Fetching 2026 Market Data...")
data = yf.download(tickers, period="2y")['Close']
corr = data.corr()

# Ward法による階層型クラスタリング
Z = linkage(corr, 'ward')

plt.figure(figsize=(12, 8))
dendrogram(Z, labels=tickers, leaf_rotation=90, distance_sort='descending')
plt.title("2026 Market: Structural Integrity (Dendrogram)")
plt.ylabel("Topological Distance")
plt.tight_layout()
plt.show()
