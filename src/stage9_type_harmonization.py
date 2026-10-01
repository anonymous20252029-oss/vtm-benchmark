"""Stage 9: String Casting & Automated LaTeX Table Formatting."""
import pandas as pd

def harmonize_types_and_export_latex(df_master, df_t1, df_t2, out_dir):
    for col in df_master.columns:
        if df_master[col].dtype == 'object':
            df_master[col] = df_master[col].astype('string')
            
    tex_t1 = df_t1.to_latex(index=False, caption="Quantitative comparative evaluation under 99.39% sparsity.", label="tab:tda_benchmark")
    tex_t2 = df_t2.to_latex(index=False, caption="Downstream link prediction benchmark.", label="tab:hgnn_eval", float_format="%.4f")
    
    with open(f"{out_dir}/Table1_Benchmark.tex", "w", encoding="utf-8") as f: f.write(tex_t1)
    with open(f"{out_dir}/Table2_HGNN.tex", "w", encoding="utf-8") as f: f.write(tex_t2)