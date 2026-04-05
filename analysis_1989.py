import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# --- 1989: The Bubble Ghost (Topological Collusion Simulation) ---
# In 1989, the market lacked structural diversity. 
# Almost all sectors moved in perfect synchronization, creating a "hollow" geometry.
tickers = [
    'NTT', 'IBJ', 'Nomura', 'Toyota', 'Sony', 
    'TEPCO', 'Sumitomo', 'Mitsui', 'Mitsubishi', 'TokioMarine'
]

def run_bubble_analysis():
    print("Generating 1989 Market Simulation (High Correlation Era)...")
    
    np.random.seed(42)
    n_days = 250  # Roughly one trading year
    n_tickers = len(tickers)
    
    # Simulate "Collusion": A single dominant market factor with very little unique variance
    # This represents the "Bubble" where diversity was lost.
    market_factor = np.random.normal(0, 0.02, n_days)
    data = {}
    for ticker in tickers:
        # 90% correlation with the market factor + 10% noise
        data[ticker] = 0.9 * market_factor + np.random.normal(0, 0.005, n_days)
        
    df = pd.DataFrame(data)
    
    # Calculate Correlation Matrix
    # In a bubble, correlations are unnaturally close to 1.0
    corr = df.corr()

    # Perform Hierarchical Clustering (Ward's Method)
    # Notice how "short" the vertical distances are compared to the 2026 model.
    Z = linkage(corr, 'ward')

    # Visualization
    plt.figure(figsize=(10, 7), facecolor='#fff5f5') # Light red background to signal "Warning/Bubble"
    
    dendrogram(
        Z, 
        labels=tickers, 
        leaf_rotation=90,
        leaf_font_size=10
    )

    plt.title("1989 Market: The Bubble Ghost (Dendrogram)", fontsize=15, pad=20)
    plt.xlabel("Simulated Asset (High Correlation)", fontsize=12)
    plt.ylabel("Topological Distance (Extremely Low)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Limitation annotation
    plt.annotate(
        'Hollow Structure: All assets merge instantly', 
        xy=(5, 0.1), 
        color='red', 
        fontsize=12,
        fontweight='bold'
    )
    
    print("Analysis complete. Displaying the 'Bubble Ghost' structure...")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_bubble_analysis()
