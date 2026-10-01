"""
End-to-End Orchestration Driver for VTM-TDA Benchmark
Author: Thi Kim-Anh Vo
"""
import os
import pandas as pd
from src.stage3_entity_resolution import resolve_and_harmonize_entities
from src.stage5_metric_space import construct_metric_space
from src.stage6_tda_homology import run_persistent_homology
from src.stage8_hypergraph_learning import evaluate_hgnn_link_prediction
from src.stage10_fair_packager import generate_zenodo_fair_metadata

def main():
    print("="*70)
    print("REPRODUCING VTM-TDA DATA ORCHESTRATION PIPELINE (STAGES 1 - 10)")
    print("="*70)
    
    # 1. Load data
    df_vi = pd.read_csv("data/ViThuoc_Master_Harmonized.csv")
    df_bai = pd.read_csv("data/BaiThuoc_Master_Harmonized.csv")
    df_cong = pd.read_csv("data/CongThuc_Master_Harmonized.csv")
    
    # 2. Metric space (Stage 5)
    H, d_mat, sparsity = construct_metric_space(df_cong)
    print(f"[Stage 5] Hypergraph Matrix: {H.shape[0]} Herbs x {H.shape[1]} Formulas | Sparsity: {sparsity*100:.2f}%")
    
    # 3. Persistent Homology (Stage 6)
    h0, h1, ent_h0, ent_h1 = run_persistent_homology(d_mat)
    print(f"[Stage 6] Persistent Invariants: {len(h0)} H0 clusters (Entropy={ent_h0:.4f}) | {len(h1)} H1 loops (Entropy={ent_h1:.4f})")
    
    # 4. HGNN Link Prediction (Stage 8)
    auc, ap, n_test = evaluate_hgnn_link_prediction(H, d_mat)
    print(f"[Stage 8] Hold-out Test (N={n_test}): HGNN AUC-ROC = {auc:.4f} | AP = {ap:.4f}")
    
    # 5. FAIR Serialization (Stage 10)
    generate_zenodo_fair_metadata("zenodo.json")
    print("[Stage 10] FAIR Metadata successfully exported to zenodo.json.")
    print("="*70)

if __name__ == "__main__":
    main()