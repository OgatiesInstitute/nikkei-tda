import yfinance as yf
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# --- 2026: The Steel Framework (14 Selected Entities) ---
# These 14 tickers represent the "pillars" of the modern Nikkei 225.
# Including Semiconductors, Finance, Trading Houses, and Shipping (9101.T).
# This diversity creates the "Steel Framework" of the current ¥53,123 valuation.
tickers = [
    '9983.T', '8035.T', '6758.T', '9984.T', '4502.T', 
    '8306.T', '8316.T', '8411.T', '8001.T', '8031.T', 
    '8058.T', '7203.T', '7267.T', '9101.T'
]

def run_analysis():
    print(f"Fetching market data for {len(tickers)} tickers from Yahoo Finance...")
    
    try:
        # Download 2 years of daily closing prices
        data = yf.download(tickers, period="2y")['Close']
        
        if data.empty:
            raise ValueError("No data fetched. Please check your internet connection or ticker symbols.")
            
        # Calculate Correlation Matrix
        # Topological distance is derived from these correlations
        corr = data.corr()

        # Perform Hierarchical Clustering using Ward's Method
        # This method minimizes the total within-cluster variance
        Z = linkage(corr, 'ward')

        # Set up the visualization
        plt.figure(figsize=(12, 8), facecolor='#f8f9fa')
        
        # distance_sort='descending' highlights the structural hierarchy
        # This organizes the tree into the "Steel Framework" architecture
        dendrogram(
            Z, 
            labels=tickers, 
            leaf_rotation=90, 
            distance_sort='descending',
            leaf_font_size=10
        )

        plt.title("2026 Nikkei 225: Structural Integrity Analysis (Dendrogram)", fontsize=15, pad=20)
        plt.xlabel("Stock Ticker", fontsize=12)
        plt.ylabel("Topological Distance (Ward)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.3)
        
        print("Analysis complete. Visualizing the 'Steel Framework'...")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    run_analysis()
