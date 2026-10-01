"""Stage 5: Sparse Hypergraph Incidence Formulation & Jaccard Metric Construction."""
import numpy as np
from scipy.spatial.distance import pdist, squareform

def construct_metric_space(df_cong):
    active_herbs = sorted(df_cong['ID_ViThuoc'].dropna().unique())
    active_prescs = sorted(df_cong['ID_BaiThuoc'].unique())
    
    h_map = {vid: i for i, vid in enumerate(active_herbs)}
    p_map = {pid: j for j, pid in enumerate(active_prescs)}

    H = np.zeros((len(active_herbs), len(active_prescs)), dtype=np.float32)
    for _, r in df_cong.iterrows():
        H[h_map[r['ID_ViThuoc']], p_map[r['ID_BaiThuoc']]] = 1.0

    sparsity = 1.0 - (np.count_nonzero(H) / H.size)
    d_jaccard = squareform(pdist(H, metric='jaccard'))
    return H, np.nan_to_num(d_jaccard, nan=1.0), sparsity