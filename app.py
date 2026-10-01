"""
VTM-TDA Benchmark: Topological Data Orchestration for Indigenous Ethnomedicine
Interactive Clinical Demonstration Platform (FAIR-Compliant AI Platform)
"""

import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="VTM-TDA Explorer",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Single-Page Viewport
st.markdown("""
<style>
    /* Compact global containers */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }
    
    /* Compact Top Banner */
    .compact-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 10px 18px;
        border-radius: 8px;
        color: white;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* Scrollable Box Container */
    .scroll-box {
        max-height: 440px;
        overflow-y: auto;
        padding-right: 6px;
    }
    
    /* Metric pill */
    .metric-pill {
        background-color: #F1F5F9;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        padding: 8px 12px;
        margin-bottom: 6px;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        margin-bottom: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 6px 14px;
        border-radius: 4px;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit padding on tables */
    div[data-testid="stTable"] {
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Compact Header Bar
st.markdown("""
<div class="compact-header">
    <div>
        <span style="font-size: 1.25rem; font-weight: 700;">🌿 VTM-TDA: Topological Data Orchestration Platform</span>
        <span style="font-size: 0.85rem; opacity: 0.8; margin-left: 12px;">AI-Ready Ethnomedicine Benchmark (Prof. Do Tat Loi)</span>
    </div>
    <div style="font-size: 0.75rem; opacity: 0.85;">
        724 Herbs | 1,635 Formulas | 99.39% Sparsity | d_B(H₁)=0.0435
    </div>
</div>
""", unsafe_allow_html=True)

# Load master harmonized datasets
@st.cache_data
def load_datasets():
    df_vi = pd.read_csv("data/ViThuoc_Master_Harmonized.csv")
    df_bai = pd.read_csv("data/BaiThuoc_Master_Harmonized.csv")
    df_cong = pd.read_csv("data/CongThuc_Master_Harmonized.csv")
    df_cross = pd.read_csv("data/ViThuoc_Global_CrossOntology_Master.csv")
    df_t1 = pd.read_csv("data/Table1_Comparative_Topological_Benchmark.csv")
    df_t2 = pd.read_csv("data/Table2_HGNN_Synergy_Prediction_Benchmark.csv")
    return df_vi, df_bai, df_cong, df_cross, df_t1, df_t2

try:
    df_vi, df_bai, df_cong, df_cross, df_t1, df_t2 = load_datasets()
except Exception as e:
    st.error(f"Error loading datasets from 'data/' directory: {e}. Please ensure data files are placed in 'data/' folder.")
    st.stop()

# Sidebar: Secondary Invariants & Details
with st.sidebar:
    st.header("📊 Benchmark Invariants")
    st.metric(label="Master Botanical Taxa", value=f"{len(df_vi):,}")
    st.metric(label="Curated Formulations", value=f"{len(df_bai):,}")
    st.metric(label="Active Links (Incidence)", value=f"{len(df_cong):,}")
    st.metric(label="Matrix Sparsity", value="99.39%", delta="Submatrix 226×410")
    st.metric(label="Persistent Clusters (H₀)", value="211", delta="Entropy: 0.9966")
    st.metric(label="Synergy Loops (H₁)", value="13", delta="Entropy: 0.9264")
    st.metric(label="Bottleneck dB(H₁)", value="0.0435", delta="Conserved vs TCM")
    st.metric(label="Bottleneck dB(H₀)", value="0.2500", delta="Tropical Divergence")
    st.caption("DOI: 10.5281/zenodo.23075404 | MIT License")

# Tabs Layout
tab_cases, tab_browser, tab_tda, tab_hgnn = st.tabs([
    "🌟 Clinical Cases",
    "🔍 Cross-Ontology Directory",
    "📐 TDA vs Baselines",
    "🧠 Link Prediction (HGNN)"
])

# ==============================================================================
# TAB 1: CLINICAL CASES (Compact Single-View)
# ==============================================================================
with tab_cases:
    col_sel, col_desc = st.columns([1.5, 3])
    with col_sel:
        case_options = {
            "Case 1: Ích Mẫu (Leonurus heterophyllus)": 1,
            "Case 2: Hương Phụ (Cyperus rotundus)": 2,
            "Case 3: Diếp Cá (Houttuynia cordata)": 5,
            "Case 4: Đương Quy (Angelica sinensis)": 17,
            "Case 5: Hồng Hoa (Carthamus tinctorius)": 6,
            "Case 6: Sinh Địa - Thục Địa (Rehmannia glutinosa)": 588
        }
        selected_case_name = st.selectbox("Select Signature Ethnomedical Taxon:", list(case_options.keys()))
        selected_id = case_options[selected_case_name]
        case_data = df_cross[df_cross['ID_ViThuoc'] == selected_id].iloc[0]
    
    with col_desc:
        st.markdown(f"**Canonical Synergy Profile:** `{case_data['TenVietNam']}` (*{case_data['Binomial']}*) — Triangulated across Western & Eastern repositories.")

    c1, c2, c3 = st.columns([1.2, 1.3, 2.0])
    
    with c1:
        st.markdown("""<div class="metric-pill">""", unsafe_allow_html=True)
        st.markdown("**🌿 Botanical Identity**")
        st.write(f"• **Family:** *{case_data.get('HoThucVat', 'N/A')}*")
        st.write(f"• **Alias:** {case_data.get('TenGoiKhac', 'None')}")
        st.write(f"• **POWO:** [Kew Record]({case_data.get('POWO_Taxon_URL', 'https://powo.science.kew.org')})")
        st.markdown("""</div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("""<div class="metric-pill">""", unsafe_allow_html=True)
        st.markdown("**🌐 Ontology & Chemistry**")
        st.write(f"• **TCM:** {case_data.get('TCM_Chinese', 'N/A')} ({case_data.get('TCM_Pinyin', 'N/A')})")
        st.write(f"• **TCMSP / IMPPAT:** `{case_data.get('TCMSP_ID', 'N/A')}` / `{case_data.get('IMPPAT_ID', 'N/A')}`")
        st.write(f"• **Compound (CID):** {case_data.get('Primary_Compound', 'N/A')} (`{int(case_data['PubChem_CID']) if pd.notna(case_data['PubChem_CID']) else 'N/A'}`)")
        st.markdown("""</div>""", unsafe_allow_html=True)

    with c3:
        st.markdown("**📜 Associated Formulations (Master Hypergraph)**")
        linked_presc_ids = df_cong[df_cong['ID_ViThuoc'] == selected_id]['ID_BaiThuoc'].unique()
        
        if len(linked_presc_ids) > 0:
            matching_prescs = df_bai[df_bai['ID_BaiThuoc'].isin(linked_presc_ids)]
            with st.container(height=260):
                for _, p_row in matching_prescs.iterrows():
                    co_herbs = df_cong[df_cong['ID_BaiThuoc'] == p_row['ID_BaiThuoc']]
                    co_details = df_vi[df_vi['ID_ViThuoc'].isin(co_herbs['ID_ViThuoc'])]
                    roster = " + ".join([f"`{h}`" for h in co_details['TenVietNam'].tolist()])
                    
                    st.markdown(f"**💊 Formula #{p_row['ID_BaiThuoc']}: {p_row['TenBaiThuoc']}**")
                    st.caption(f"**Indication:** {p_row['ChuTri']} | **Source:** {p_row['NguonGoc']}")
                    st.markdown(f"**Roster:** {roster}")
                    st.divider()
        else:
            st.info("Monographic ethnomedical taxon without compound formulations.")

# ==============================================================================
# TAB 2: CROSS-ONTOLOGY BROWSER (Direct Grid)
# ==============================================================================
with tab_browser:
    col_q1, col_q2, col_ck = st.columns([2, 2, 1.2])
    with col_q1:
        search_txt = st.text_input("Search Vietnamese Name / Alias:", placeholder="e.g., Ba Kich, Sam...", label_visibility="collapsed")
    with col_q2:
        search_sci = st.text_input("Search Latin Binomial / Compound:", placeholder="e.g., Panax, Quercetin...", label_visibility="collapsed")
    with col_ck:
        only_mapped = st.checkbox("Only Globally Mapped", value=False)

    filtered_df = df_cross.copy()
    if search_txt:
        filtered_df = filtered_df[filtered_df['TenVietNam'].str.contains(search_txt, case=False, na=False) | 
                                  filtered_df['TenGoiKhac'].str.contains(search_txt, case=False, na=False)]
    if search_sci:
        filtered_df = filtered_df[filtered_df['Binomial'].str.contains(search_sci, case=False, na=False) | 
                                  filtered_df['Primary_Compound'].str.contains(search_sci, case=False, na=False)]
    if only_mapped:
        filtered_df = filtered_df[filtered_df['TCMSP_ID'].notna()]

    cols_to_show = ['ID_ViThuoc', 'TenVietNam', 'Binomial', 'TCM_Pinyin', 'TCM_Chinese', 'TCMSP_ID', 'Primary_Compound', 'PubChem_CID', 'IMPPAT_ID']
    st.dataframe(
        filtered_df[cols_to_show].rename(columns={
            'ID_ViThuoc': 'ID', 'TenVietNam': 'Vietnamese Name', 'Binomial': 'Latin Binomial',
            'TCM_Pinyin': 'Pinyin', 'TCM_Chinese': 'Hanzi', 'TCMSP_ID': 'TCMSP',
            'Primary_Compound': 'Compound', 'PubChem_CID': 'PubChem CID', 'IMPPAT_ID': 'IMPPAT'
        }),
        use_container_width=True,
        height=380
    )
    st.caption("Curation Audit: 81.22% (588 taxa) matched NCBI Taxonomy; 13.54% (98 taxa) matched PubChem CIDs; remainder under Valid_Missing_Ethnomedical.")

# ==============================================================================
# TAB 3: TDA VS BASELINES (Side-by-Side Comparison)
# ==============================================================================
with tab_tda:
    col_tda_tbl, col_tda_info = st.columns([1.5, 1])
    
    with col_tda_tbl:
        st.markdown("**Table 1: Comparative Evaluation Under 99.39% Sparsity**")
        st.dataframe(df_t1, use_container_width=True, height=270)
        
    with col_tda_info:
        st.markdown("**🔬 Simplicial Homology & Manifold Alignment**")
        st.markdown("""
        * **H₀ Connected Clusters:** **211 Persistent Features** (Entropy: **0.9966**)
        * **H₁ Synergy Cavities:** **13 Non-Bounding Loops** (Entropy: **0.9264**)
        * **Filtration Interval:** Invariant across $\epsilon \in [0.80, 0.99]$
        * **Alignment vs TCM:**
          - **$d_B(H_1) = 0.0435$**: Strictly conserved combinatorial synergy motifs
          - **$d_B(H_0) = 0.2500$**: Biogeographical tropical flora speciation
        """)
        st.caption("Vietoris–Rips filtrations preserve multi-body simplicial geometry where PCA loses 91.45% of variance.")

# ==============================================================================
# TAB 4: HYPERGRAPH LINK PREDICTION (Clean Benchmark Card)
# ==============================================================================
with tab_hgnn:
    col_hgnn_tbl, col_hgnn_res = st.columns([1.3, 1])
    
    with col_hgnn_tbl:
        st.markdown("**Table 2: Downstream Evaluation (Hold-out Test Set N=106, 80/20 Non-Leaky Split)**")
        st.dataframe(df_t2, use_container_width=True, height=140)
        
    with col_hgnn_res:
        st.success("""
        **Performance Summary:**
        • **Topological HGNN (Ours):** AUC-ROC = **1.0000** | AP = **1.0000**  
        • **Pairwise Baseline (GCN):** AUC-ROC = **0.8270** | AP = **0.8302**  
        • **Relative Gain:** **+17.30%** over standard pairwise convolution.
        """)
        st.info("Simplicial boundary operators prevent Laplacian oversmoothing over sparse bipartite structures.")
