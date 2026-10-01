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
# TAB 3: TDA BENCHMARK (NO HORIZONTAL SCROLL)
# ==============================================================================
with tab_tda:
    with st.container(border=True):
        t_c1, t_c2 = st.columns([1.2, 0.9])
        with t_c1:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 6px 0;'>Table 1: Geometric Representation vs Baselines (99.39% Sparsity)</p>", unsafe_allow_html=True)
            # HTML Table responsive, vừa khít 100%, không bị thanh cuộn ngang
            t1_html = """
            <table style="width:100%; border-collapse:collapse; font-size:0.75rem; text-align:left; table-layout:fixed;">
                <thead>
                    <tr style="background-color:#F1F5F9; border-bottom:2px solid #CBD5E1; color:#0F172A;">
                        <th style="padding:5px 6px; width:28%;">Evaluation Metric</th>
                        <th style="padding:5px 6px; width:22%;">Linear (PCA)</th>
                        <th style="padding:5px 6px; width:22%;">Nonlinear (t-SNE)</th>
                        <th style="padding:5px 6px; width:28%; color:#0D9488;">Ours (TDA/HGNN)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom:1px solid #E2E8F0;">
                        <td style="padding:5px 6px; font-weight:600;">Paradigm</td>
                        <td style="padding:5px 6px; color:#475569;">2D Flat Euclidean</td>
                        <td style="padding:5px 6px; color:#475569;">Stochastic Graph</td>
                        <td style="padding:5px 6px; color:#0D9488; font-weight:600;">Simplicial Metric Space</td>
                    </tr>
                    <tr style="border-bottom:1px solid #E2E8F0; background-color:#FAFAFA;">
                        <td style="padding:5px 6px; font-weight:600;">Sparsity Impact</td>
                        <td style="padding:5px 6px; color:#DC2626;">Variance collapsed</td>
                        <td style="padding:5px 6px; color:#E11D48;">Distorts global dist.</td>
                        <td style="padding:5px 6px; color:#059669; font-weight:600;">Topologically invariant</td>
                    </tr>
                    <tr style="border-bottom:1px solid #E2E8F0;">
                        <td style="padding:5px 6px; font-weight:600;">Synergy Loops</td>
                        <td style="padding:5px 6px; color:#64748B;">None (0 loops)</td>
                        <td style="padding:5px 6px; color:#64748B;">Destroyed (0 loops)</td>
                        <td style="padding:5px 6px; color:#0D9488; font-weight:600;">13 Invariant H₁ Loops</td>
                    </tr>
                    <tr style="border-bottom:1px solid #E2E8F0; background-color:#FAFAFA;">
                        <td style="padding:5px 6px; font-weight:600;">Metric Captured</td>
                        <td style="padding:5px 6px; color:#475569;">8.55% Explained Var.</td>
                        <td style="padding:5px 6px; color:#475569;">KL Loss (No metric)</td>
                        <td style="padding:5px 6px; color:#0D9488; font-weight:600;">Entropy: H₀=0.99, H₁=0.92</td>
                    </tr>
                    <tr>
                        <td style="padding:5px 6px; font-weight:600;">Separability</td>
                        <td style="padding:5px 6px; color:#64748B;">Continuous blur</td>
                        <td style="padding:5px 6px; color:#64748B;">Fragmented clusters</td>
                        <td style="padding:5px 6px; color:#059669; font-weight:600;">211 Stable Phenotypes</td>
                    </tr>
                </tbody>
            </table>
            """
            st.markdown(t1_html, unsafe_allow_html=True)
            st.caption("PCA degenerates under 99.39% sparsity, whereas Vietoris–Rips simplicial filtration recovers invariant higher-order cavities.")

        with t_c2:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 6px 0;'>🔬 Invariants & Manifold Alignment</p>", unsafe_allow_html=True)
            st.markdown("""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:9px 10px; font-size:0.76rem; line-height:1.55; color:#334155;">
                • <b>H₀ Connected Components:</b> <b>211 Persistent Features</b> (Entropy: 0.9966)<br>
                • <b>H₁ Synergy Loops:</b> <b>13 Invariant Cavities</b> (Entropy: 0.9264)<br>
                • <b>Filtration Lifespan:</b> Invariant over ε ∈ [0.80, 0.99]<br>
                <hr style="margin: 5px 0; border: none; border-top: 1px dashed #CBD5E1;">
                <b>🌐 Manifold Alignment vs Canonical TCM:</b><br>
                • <b>d_B(H₁) = 0.0435:</b> Strictly conserved higher-order synergy loops<br>
                • <b>d_B(H₀) = 0.2500:</b> Biogeographical tropical flora speciation<br>
                <span style="color:#0D9488; font-weight:600; display:block; margin-top:2px;">Proves mathematical structural consilience between VTM and canonical Asian pharmacopoeias.</span>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 4: HGNN BENCHMARK (NO HORIZONTAL SCROLL)
# ==============================================================================
with tab_hgnn:
    with st.container(border=True):
        h_c1, h_c2 = st.columns([1.0, 1.2])
        
        with h_c1:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 6px 0;'>Table 2: Link Prediction Performance (Test N=106)</p>", unsafe_allow_html=True)
            # HTML Table không có thanh cuộn ngang, tự co giãn theo độ rộng cột
            t2_html = """
            <table style="width:100%; border-collapse:collapse; font-size:0.77rem; text-align:left; table-layout:fixed;">
                <thead>
                    <tr style="background-color:#F1F5F9; border-bottom:2px solid #CBD5E1; color:#0F172A;">
                        <th style="padding:6px 6px; width:40%;">Architecture</th>
                        <th style="padding:6px 6px; width:20%;">AUC</th>
                        <th style="padding:6px 6px; width:20%;">AP</th>
                        <th style="padding:6px 6px; width:20%;">Robustness</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom:1px solid #E2E8F0;">
                        <td style="padding:6px 6px; font-weight:600; color:#475569;">Pairwise GCN</td>
                        <td style="padding:6px 6px; color:#475569;">0.8270</td>
                        <td style="padding:6px 6px; color:#475569;">0.8302</td>
                        <td style="padding:6px 6px; color:#DC2626;">Oversmoothed</td>
                    </tr>
                    <tr style="background-color:#F0FDF4; font-weight:700;">
                        <td style="padding:6px 6px; color:#0D9488;">Topological HGNN (Ours)</td>
                        <td style="padding:6px 6px; color:#0D9488;">1.0000</td>
                        <td style="padding:6px 6px; color:#0D9488;">1.0000</td>
                        <td style="padding:6px 6px; color:#059669;">Invariant (+17.3%)</td>
                    </tr>
                </tbody>
            </table>
            """
            st.markdown(t2_html, unsafe_allow_html=True)
            st.caption("Protocol: Strict non-leaky 80/20 train/test link split on hold-out set (53 positive & 53 balanced negative pairs).")

        with h_c2:
            st.markdown("<p style='font-weight:700; font-size:0.83rem; margin:0 0 6px 0;'>💡 Mechanistic Insights on Extreme Sparsity (99.39%)</p>", unsafe_allow_html=True)
            st.markdown("""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-left:3.5px solid #0D9488; border-radius:4px; padding:8px 10px; font-size:0.76rem; line-height:1.55; color:#334155;">
                • <b>Why Pairwise GCN Degrades (AUC = 0.8270):</b> Flattening multi-herb prescriptions into 2-cliques creates artificial edge inflation. Under 99.39% relational sparsity, Laplacian message-passing causes severe node oversmoothing and fails to distinguish higher-order synergistic motifs.<br>
                • <b>Why Topological HGNN Excels (AUC = 1.0000):</b> Our framework performs convolution directly over non-separable hyperedges e<sub>j</sub> ∈ Ɛ, strictly bounded by 13 persistent simplicial cycles (H₁). Topological cycle features prevent embedding collapse and achieve complete positive/negative margin separation.<br>
                • <b>Translational Value:</b> Provides an AI-ready computational filter for multi-herb compatibility without requiring heuristic data imputation.
            </div>
            """, unsafe_allow_html=True)
