"""Stage 6: Persistent Simplicial Homology Filtration via GUDHI."""
import gudhi as gd
import numpy as np

def compute_persistence_entropy(intervals):
    lifetimes = np.array([d - b for b, d in intervals if d > b and not np.isinf(d)])
    if len(lifetimes) == 0 or np.sum(lifetimes) == 0: return 0.0
    p = lifetimes / np.sum(lifetimes)
    entropy = -np.sum(p * np.log2(p + 1e-15))
    return float(entropy / np.log2(len(p))) if len(p) > 1 else 1.0

def run_persistent_homology(dist_matrix):
    rips = gd.RipsComplex(distance_matrix=dist_matrix, max_edge_length=1.0)
    st = rips.create_simplex_tree(max_dimension=2)
    st.persistence()

    h0 = np.array([[b, min(d, 1.0)] for b, d in st.persistence_intervals_in_dimension(0) if not np.isinf(b)])
    h1 = np.array([[b, min(d, 1.0)] for b, d in st.persistence_intervals_in_dimension(1) if not np.isinf(b)])

    ent_h0 = compute_persistence_entropy(h0)
    ent_h1 = compute_persistence_entropy(h1)
    return h0, h1, ent_h0, ent_h1