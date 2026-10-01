"""
VTM-TDA Benchmark: Topological Data Orchestration for Indigenous Ethnomedicine
Executive Single-Page Clinical Dashboard (FAIR-Compliant Platform)
Author: Thi Kim-Anh Vo
"""

import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="VTM-TDA Executive Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling: Modern Executive Bio-Informatics Palette
st.markdown("""
<style>
    /* 1. Global Viewport Fitting */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        height: 100vh !important;
        background-color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .main .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0.4rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 100% !important;
        height: 100vh;
    }
    
    /* Hide collapsed sidebar control button */
    [data-testid="collapsedControl"] { display: none !important; }

    /* 2. Centered Header */
    .hero-title {
        text-align: center;
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin: 0;
        line-height: 1.2;
    }
    .hero-sub {
        text-align: center;
        font-size: 0.78rem;
        color: #475569;
        margin: 2px 0 8px 0;
    }

    /* 3. Horizontal KPI Ribbon */
    .kpi-ribbon {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        background: #FFFFFF;
        padding: 8px 12px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        margin-bottom: 8px;
    }
    .kpi-card {
        text-align: center;
        border-right: 1px solid #F1F5F9;
        padding: 0 4px;
    }
    .kpi-card:last-child { border-right: none; }
    .kpi-label {
        font-size: 0.65rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        display: block;
        margin-bottom: 1px;
    }
    .kpi-val {
        font-size: 1.12rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.1;
    }
    .kpi-sub {
        font-size: 0.64rem;
        color: #0D9488;
        font-weight: 600;
        display: block;
        margin-top: 1px;
    }

    /* 4. Tab Header Polish */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px !important;
        margin-bottom: 8px !important;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 5px 14px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        border-radius: 6px !important;
        color: #475569 !important;
    }
    .stTabs [aria-selected="true"] {
        color: #0D9488 !important;
        background-color: #F0FDFA !important;
    }

    /* 5. Formula Cards */
    .formula-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 3.5px solid #0D9488;
        border-radius: 4px;
        padding: 6px 9px;
        margin-bottom: 6px;
        font-size: 0.77rem;
    }
    .formula-card-title {
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 2px;
    }
</style>
""", unsafe_allow_html=True)

# 1. Centered Header (Journal Info Removed)
st.markdown("""
<div class="hero-title">🌿 VTM-TDA: Topological Data Orchestration Framework</div>
<div class="hero-sub">AI-Ready Benchmark & Hypergraph Learning for Vietnamese Traditional Medicine (Prof. Do Tat Loi Pharmacopoeia)</div>
""", unsafe_allow_html=True)

# 2. Data Loader
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
    st.error(f"Error loading datasets from 'data/' directory: {e}")
    st.stop()

# 3. Horizontal KPI Ribbon
st.markdown(f"""
<div class="kpi-ribbon">
    <div class="kpi-card">
        <span class="kpi-label">Master Taxa</span>
        <span class="kpi-val">{len(df_vi):,}</span>
        <span class="kpi-sub">81.22% NCBI TaxID</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">Formulations</span>
        <span class="kpi-val">{len(df_bai):,}</span>
        <span class="kpi-sub">Audited 100%</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">Hyperedges</span>
        <span class="kpi-val">{len(df_cong):,}</span>
        <span class="kpi-sub">Submatrix 226×410</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">Matrix Sparsity</span>
        <span class="kpi-val">99.39%</span>
        <span class="kpi-sub" style="color:#E11D48;">Severe Sparsity</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">H₀ Clusters</span>
        <span class="kpi-val">211</span>
        <span class="kpi-sub">Entropy: 0.9966</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">H₁ Synergy Loops</span>
        <span class="kpi-val">13</span>
        <span class="kpi-sub">d_B(H₁) = 0.0435</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">HGNN Link Pred.</span>
        <span class="kpi-val">1.0000</span>
        <span class="kpi-sub">AUC (vs GCN 0.827)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Main Functional Tabs
tab_cases, tab_browser, tab_tda, tab_hgnn = st.tabs([
    "🌟 Clinical Case Explorer",
    "🔍 Cross-Ontology Directory",
    "📐 TDA vs Baselines Benchmark",
    "🧠 HGNN Synergy Link Prediction"
])

# ==============================================================================
# TAB 1: 3-COLUMN CLINICAL CASE EXPLORER
# ==============================================================================
with tab_cases:
    case_options = {
        "Case 1: Ích Mẫu (Leonurus heterophyllus)": 1,
        "Case 2: Hương Phụ (Cyperus rotundus)": 2,
        "Case 3: Diếp Cá (Houttuynia cordata)": 5,
        "Case 4: Đương Quy (Angelica sinensis)": 17,
        "Case 5: Hồng Hoa (Carthamus tinctorius)": 6,
        "Case 6: Sinh Địa - Thục Địa (Rehmannia glutinosa)": 588
    }

    col_1, col_2, col_3 = st.columns([1.1, 1.1, 1.8])

    # COLUMN 1: Botanical & Taxonomic Identity
    with col_1:
        with st.container(border=True):
            st.markdown("<p style='font-weight:700; font-size:0.84rem; color:#0F172A; margin:0 0 4px 0;'>🌿 Botanical Identity</p>", unsafe_allow_html=True)
            selected_name = st.selectbox("Select Signature Taxon:", list(case_options.keys()), label_visibility="collapsed")
            selected_id = case_options[selected_name]
            c_data = df_cross[df_cross['ID_ViThuoc'] == selected_id].iloc[0]

            st.markdown(f"""
            <div style="font-size:0.77rem; line-height: 1.55; color:#334155;">
                <b>• Vernacular:</b> <span style="color:#0D9488; font-weight:700;">{c_data['TenVietNam']}</span><br>
                <b>• Binomial (POWO):</b> <i>{c_data['Binomial']}</i><br>
                <b>• Plant Family:</b> {c_data.get('HoThucVat', 'N/A')}<br>
                <b>• Folk Aliases:</b> {str(c_data.get('TenGoiKhac', 'None'))[:32]}<br>
                <b>• POWO Record:</b> <a href="{c_data.get('POWO_Taxon_URL', 'https://powo.science.kew.org')}" target="_blank" style="color:#0284C7;">Kew Royal Gardens</a><br>
                <b>• NCBI Taxonomy:</b> <code>{c_data.get('NCBI_TaxID', 'Verified')}</code>
            </div>
            """, unsafe_allow_html=True)

    # COLUMN 2: Chemical & Energetics Cross-Mapping
    with col_2:
        with st.container(border=True):
            st.markdown("<p style='font-weight:700; font-size:0.84rem; color:#0F172A; margin:0 0 4px 0;'>🌐 Chemistry & Energetics</p>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="font-size:0.77rem; line-height: 1.55; color:#334155;">
                <b>• TCM Equiv.:</b> {c_data.get('TCM_Chinese', 'N/A')} ({c_data.get('TCM_Pinyin', 'N/A')})<br>
                <b>• TCMSP ID:</b> <code>{c_data.get('TCMSP_ID', 'N/A')}</code><br>
                <b>• IMPPAT ID:</b> <code>{c_data.get('IMPPAT_ID', 'N/A')}</code><br>
                <b>• Primary Compound:</b> <b>{c_data.get('Primary_Compound', 'N/A')}</b><br>
                <b>• PubChem CID:</b> <code>{int(c_data['PubChem_CID']) if pd.notna(c_data['PubChem_CID']) else 'N/A'}</code><br>
                <hr style="margin: 4px 0; border: none; border-top: 1px dashed #E2E8F0;">
                <b>• Nature & Flavor:</b> {c_data.get('TinhVi', 'N/A')}<br>
                <b>• Meridian Tropisms:</b> <code>{c_data.get('QuyKinh', 'N/A')}</code><br>
                <b>• Clinical Dosage:</b> {c_data.get('LieuDung', '6-12g/day')}
            </div>
            """, unsafe_allow_html=True)

    # COLUMN 3: Clinical Prescriptions (Master Hypergraph)
    with col_3:
        with st.container(border=True):
            linked_ids = df_cong[df_cong['ID_ViThuoc'] == selected_id]['ID_BaiThuoc'].unique()
            matching_prescs = df_bai[df_bai['ID_BaiThuoc'].isin(linked_ids)]
            
            st.markdown(f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-weight:700; font-size:0.84rem; color:#0F172A;">📜 Formulations in Master Hypergraph</span>
                <span style="font-size:0.72rem; color:#0D9488; font-weight:600;">{len(matching_prescs)} Linked Prescriptions</span>
            </div>
            """, unsafe_allow_html=True)

            with st.container(height=320):
                if len(matching_prescs) > 0:
                    for _, p_row in matching_prescs.iterrows():
                        co_herbs = df_cong[df_cong['ID_BaiThuoc'] == p_row['ID_BaiThuoc']]
                        co_details = df_vi[df_vi['ID_ViThuoc'].isin(co_herbs['ID_ViThuoc'])]
                        roster = " + ".join([f"<span style='color:#0F766E; font-weight:600;'>{h}</span>" for h in co_details['TenVietNam'].tolist()])
                        
                        st.markdown(f"""
                        <div class="formula-card">
                            <div class="formula-card-title">💊 #{p_row['ID_BaiThuoc']}: {p_row['TenBaiThuoc']}</div>
                            <div style="color:#64748B; font-size:0.72rem; margin:1px 0;"><b>Indications:</b> {p_row.get('ChuTri', 'Standard indication')} | <b>Source:</b> {p_row.get('NguonGoc', 'Prof. Do Tat Loi')}</div>
                            <div style="font-size:0.72rem; margin-top:2px;"><b>Herb Roster:</b> {roster}</div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("Monographic taxon documented without complex multi-herb co-occurrences.")

# ==============================================================================
# TAB 2: DIRECTORY BROWSER
# ==============================================================================
with tab_browser:
    with st.container(border=True):
        f1, f2, f3 = st.columns([1.5, 1.5, 1.0])
        with f1:
            s_vn = st.text_input("Filter Vernacular Name:", placeholder="Type vernacular name (e.g., Ba Kich)...", label_visibility="collapsed")
        with f2:
            s_latin = st.text_input("Filter Latin / Compound:", placeholder="Type Latin binomial or compound...", label_visibility="collapsed")
        with f3:
            ck_mapped = st.checkbox("Only Globally Triangulated", value=False)

        df_view = df_cross.copy()
        if s_vn:
            df_view = df_view[df_view['TenVietNam'].str.contains(s_vn, case=False, na=False)]
        if s_latin:
            df_view = df_view[df_view['Binomial'].str.contains(s_latin, case=False, na=False) | 
                              df_view['Primary_Compound'].str.contains(s_latin, case=False, na=False)]
        if ck_mapped:
            df_view = df_view[df_view['TCMSP_ID'].notna()]

        st.dataframe(
            df_view[['ID_ViThuoc', 'TenVietNam', 'Binomial', 'TCM_Chinese', 'TCMSP_ID', 'Primary_Compound', 'PubChem_CID', 'IMPPAT_ID']].rename(columns={
                'ID_ViThuoc': 'ID', 'TenVietNam': 'Vernacular Name', 'Binomial': 'Latin Binomial',
                'TCM_Chinese': 'TCM Hanzi', 'TCMSP_ID': 'TCMSP ID', 'Primary_Compound': 'Primary Compound', 'PubChem_CID': 'PubChem CID', 'IMPPAT_ID': 'IMPPAT ID'
            }),
            use_container_width=True,
            height=300
        )
        st.caption("Curation Audit: 81.22% (588/724) NCBI Taxonomy match; 13.54% (98/724) isolated PubChem CIDs; remaining taxa tracked via Valid_Missing_Ethnomedical.")

# ==============================================================================
# TAB 3: TDA BENCHMARK
# ==============================================================================
with tab_tda:
    with st.container(border=True):
        t_c1, t_c2 = st.columns([1.5, 1.0])
        with t_c1:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 4px 0;'>Table 1: Comparative Dimensionality Reduction (99.39% Sparsity)</p>", unsafe_allow_html=True)
            st.dataframe(df_t1, use_container_width=True, height=255)
        with t_c2:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 4px 0;'>🔬 Persistent Invariants & Alignment</p>", unsafe_allow_html=True)
            st.markdown("""
            <div style="font-size:0.77rem; line-height: 1.55; color:#334155;">
                • <b>H₀ Connected Components:</b> <b>211 Persistent Features</b> (Entropy: 0.9966)<br>
                • <b>H₁ Synergy Loops:</b> <b>13 Non-Bounding Cavities</b> (Entropy: 0.9264)<br>
                • <b>Filtration Interval:</b> Invariant over ε ∈ [0.80, 0.99]<br>
                <hr style="margin: 4px 0; border: none; border-top: 1px dashed #E2E8F0;">
                <b>🌐 Manifold Alignment vs Canonical TCM:</b><br>
                • <b>d_B(H₁) = 0.0435:</b> Strictly conserved higher-order synergy loops<br>
                • <b>d_B(H₀) = 0.2500:</b> Biogeographical tropical flora speciation<br>
                <span style="color:#0D9488; font-weight:600;">Validates structural equivalence between VTM and canonical Asian pharmacopoeias.</span>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 4: HGNN BENCHMARK
# ==============================================================================
with tab_hgnn:
    with st.container(border=True):
        h_c1, h_c2 = st.columns([1.3, 1.0])
        with h_c1:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 4px 0;'>Table 2: Link Prediction Benchmark (Hold-out Test Set N=106, 80/20 Edge Split)</p>", unsafe_allow_html=True)
            st.dataframe(df_t2, use_container_width=True, height=135)
        with h_c2:
            st.markdown("""
            <div style="background:#F0FDFA; border:1px solid #CCFBF1; border-left:3.5px solid #0D9488; border-radius:4px; padding:8px 10px; font-size:0.78rem; line-height:1.5;">
                <b style="color:#0F766E;">Performance Evaluation Summary</b><br>
                • <b>Topological HGNN (Ours):</b> AUC-ROC = <b>1.0000</b> | AP = <b>1.0000</b><br>
                • <b>Pairwise Baseline (GCN):</b> AUC-ROC = <b>0.8270</b> | AP = <b>0.8302</b><br>
                • <b>Relative Improvement:</b> <b>+17.30%</b> gain under 99.39% sparsity.<br>
                <span style="color:#64748B; font-size:0.72rem;">Simplicial boundary operators prevent Laplacian oversmoothing collapsed by pairwise graphs.</span>
            </div>
            """, unsafe_allow_html=True)
