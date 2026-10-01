"""
VTM-TDA Benchmark: Topological Data Orchestration for Indigenous Ethnomedicine
Executive Single-Page Clinical Dashboard (FAIR-Compliant Platform)
Author: Thi Kim-Anh Vo
"""

import streamlit as st
import pandas as pd
import numpy as np

# Cấu hình trang toàn màn hình, đóng hoàn toàn sidebar
st.set_page_config(
    page_title="VTM-TDA Executive Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS ép toàn bộ giao diện vừa khít 1 Viewport không scroll
st.markdown("""
<style>
    /* 1. Triệt tiêu khoảng trống thừa của Streamlit */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        height: 100vh !important;
        background-color: #F8FAFC;
    }
    .main .block-container {
        padding: 0.6rem 1.5rem 0.2rem 1.5rem !important;
        max-width: 100% !important;
        height: 100vh;
    }
    
    /* Ẩn hoàn toàn nút mở sidebar */
    [data-testid="collapsedControl"] { display: none !important; }

    /* 2. Centered Header */
    .hero-header {
        text-align: center;
        margin-bottom: 6px;
    }
    .hero-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin: 0;
    }
    .hero-sub {
        font-size: 0.78rem;
        color: #475569;
        margin-top: 1px;
    }

    /* 3. Horizontal Metric Ribbon (Băng ngang 1 dòng trên cùng) */
    .kpi-ribbon {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        background: #FFFFFF;
        padding: 6px 10px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
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
        display: block;
        line-height: 1.1;
    }
    .kpi-val {
        font-size: 1.05rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.2;
    }
    .kpi-sub {
        font-size: 0.62rem;
        color: #059669;
        font-weight: 600;
        display: block;
    }

    /* 4. Tab Bar căn chỉnh thanh lịch */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px !important;
        margin-bottom: 6px !important;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 4px 14px !important;
        font-size: 0.82rem !important;
        border-radius: 6px !important;
        font-weight: 600;
    }

    /* 5. Executive Panels */
    .exec-panel {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 10px 12px;
        height: calc(100vh - 195px);
        box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        overflow-y: auto;
    }
    .panel-header {
        font-size: 0.82rem;
        font-weight: 700;
        color: #0F172A;
        border-bottom: 2px solid #F1F5F9;
        padding-bottom: 4px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* 6. Formula Cards bên trong Cột 3 */
    .formula-badge {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 3px solid #0D9488;
        border-radius: 4px;
        padding: 6px 8px;
        margin-bottom: 6px;
        font-size: 0.76rem;
    }
    .formula-title {
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 2px;
    }
</style>
""", unsafe_allow_html=True)

# 1. Header ở giữa trang
st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">🌿 VTM-TDA: Topological Data Orchestration Framework</h1>
    <p class="hero-sub">AI-Ready Benchmark & Hypergraph Learning for Vietnamese Traditional Medicine (Prof. Do Tat Loi Pharmacopoeia)</p>
</div>
""", unsafe_allow_html=True)

# Nạp dữ liệu
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
    st.error(f"Error loading datasets: {e}")
    st.stop()

# 2. BĂNG THÔNG SỐ NGANG 1 DÒNG (Top Metric Ribbon)
st.markdown(f"""
<div class="kpi-ribbon">
    <div class="kpi-card">
        <span class="kpi-label">Master Taxa</span>
        <span class="kpi-val">{len(df_vi):,}</span>
        <span class="kpi-sub">81.22% NCBI</span>
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
        <span class="kpi-sub" style="color:#DC2626;">Extreme Sparse</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-label">H₀ Clusters</span>
        <span class="kpi-val">211</span>
        <span class="kpi-sub">Entropy 0.9966</span>
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

# 3. Main Navigation
tab_cases, tab_browser, tab_tda, tab_hgnn = st.tabs([
    "🌟 Clinical Case Explorer",
    "🔍 Multi-Tier Cross-Ontology Directory",
    "📐 TDA vs Baselines Benchmark",
    "🧠 HGNN Synergy Link Prediction"
])

# ==============================================================================
# TAB 1: BỐ CỤC 3 CỘT THÔNG MINH TRÊN 1 HÀNG
# ==============================================================================
with tab_cases:
    col_1, col_2, col_3 = st.columns([1.1, 1.1, 1.8])

    # Case dictionary
    case_options = {
        "Ích Mẫu (Leonurus heterophyllus)": 1,
        "Hương Phụ (Cyperus rotundus)": 2,
        "Diếp Cá (Houttuynia cordata)": 5,
        "Đương Quy (Angelica sinensis)": 17,
        "Hồng Hoa (Carthamus tinctorius)": 6,
        "Sinh Địa - Thục Địa (Rehmannia glutinosa)": 588
    }

    # CỘT 1: Danh pháp & Thực vật
    with col_1:
        st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-header"><span>🌿 Botanical Identity</span></div>', unsafe_allow_html=True)
        
        selected_name = st.selectbox("Select Signature Taxon:", list(case_options.keys()), label_visibility="collapsed")
        selected_id = case_options[selected_name]
        c_data = df_cross[df_cross['ID_ViThuoc'] == selected_id].iloc[0]

        st.markdown(f"""
        <div style="font-size:0.78rem; line-height: 1.6; margin-top: 6px;">
            <b>• Vernacular:</b> <span style="color:#0D9488; font-weight:700;">{c_data['TenVietNam']}</span><br>
            <b>• Latin Binomial:</b> <i>{c_data['Binomial']}</i><br>
            <b>• Plant Family:</b> {c_data.get('HoThucVat', 'N/A')}<br>
            <b>• Folk Aliases:</b> {str(c_data.get('TenGoiKhac', 'None'))[:35]}<br>
            <b>• Kew POWO:</b> <a href="{c_data.get('POWO_Taxon_URL', 'https://powo.science.kew.org')}" target="_blank">POWO Link</a><br>
            <b>• NCBITaxID:</b> <code>{c_data.get('NCBI_TaxID', 'Verified')}</code>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # CỘT 2: Hóa sinh & Đông y Triangulation
    with col_2:
        st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-header"><span>🌐 Chemistry & Energetics</span></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="font-size:0.78rem; line-height: 1.6;">
            <b>• TCM Equiv.:</b> {c_data.get('TCM_Chinese', 'N/A')} ({c_data.get('TCM_Pinyin', 'N/A')})<br>
            <b>• TCMSP ID:</b> <code>{c_data.get('TCMSP_ID', 'N/A')}</code><br>
            <b>• IMPPAT ID:</b> <code>{c_data.get('IMPPAT_ID', 'N/A')}</code><br>
            <b>• Active Compound:</b> <b>{c_data.get('Primary_Compound', 'N/A')}</b><br>
            <b>• PubChem CID:</b> <code>{int(c_data['PubChem_CID']) if pd.notna(c_data['PubChem_CID']) else 'N/A'}</code><br>
            <hr style="margin: 6px 0; border: none; border-top: 1px dashed #E2E8F0;">
            <b>• Tính Vị:</b> {c_data.get('TinhVi', 'N/A')}<br>
            <b>• Quy Kinh:</b> <code>{c_data.get('QuyKinh', 'N/A')}</code><br>
            <b>• Clinical Dosage:</b> {c_data.get('LieuDung', '6-12g/day')}
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # CỘT 3: Siêu đồ thị & Công thức phối ngũ liên quan
    with col_3:
        st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
        linked_ids = df_cong[df_cong['ID_ViThuoc'] == selected_id]['ID_BaiThuoc'].unique()
        matching_prescs = df_bai[df_bai['ID_BaiThuoc'].isin(linked_ids)]
        
        st.markdown(f"""
        <div class="panel-header">
            <span>📜 Clinical Formulations (Master Hypergraph)</span>
            <span style="font-size:0.7rem; color:#0D9488;">{len(matching_prescs)} Prescriptions Found</span>
        </div>
        """, unsafe_allow_html=True)

        if len(matching_prescs) > 0:
            for _, p_row in matching_prescs.iterrows():
                co_herbs = df_cong[df_cong['ID_BaiThuoc'] == p_row['ID_BaiThuoc']]
                co_details = df_vi[df_vi['ID_ViThuoc'].isin(co_herbs['ID_ViThuoc'])]
                roster = " + ".join([f"<span style='color:#0D9488; font-weight:600;'>{h}</span>" for h in co_details['TenVietNam'].tolist()])
                
                st.markdown(f"""
                <div class="formula-badge">
                    <div class="formula-title">💊 #{p_row['ID_BaiThuoc']}: {p_row['TenBaiThuoc']}</div>
                    <div style="color:#64748B; font-size:0.72rem; margin:1px 0;"><b>Indication:</b> {p_row.get('ChuTri', 'Standard indication')} | <b>Source:</b> {p_row.get('NguonGoc', 'Đỗ Tất Lợi')}</div>
                    <div style="font-size:0.72rem; margin-top:3px;"><b>Co-occurring Roster:</b> {roster}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<p style='font-size:0.78rem; color:#64748B; padding:10px;'>Monographic taxon without multi-herb formula interactions.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 2: DIRECTORY BROWSER
# ==============================================================================
with tab_browser:
    st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([1.5, 1.5, 1.0])
    with f1:
        s_vn = st.text_input("Filter Vietnamese:", placeholder="Type Vietnamese name...", label_visibility="collapsed")
    with f2:
        s_latin = st.text_input("Filter Latin/Compound:", placeholder="Type Latin/Compound...", label_visibility="collapsed")
    with f3:
        ck_mapped = st.checkbox("Only Triangulated", value=False)

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
            'ID_ViThuoc': 'ID', 'TenVietNam': 'Vietnamese', 'Binomial': 'Latin Binomial',
            'TCM_Chinese': 'TCM Hanzi', 'TCMSP_ID': 'TCMSP', 'Primary_Compound': 'Compound', 'PubChem_CID': 'PubChem CID'
        }),
        use_container_width=True,
        height=320
    )
    st.caption("Curation Audit: 81.22% (588/724) NCBI Taxonomy concordance; 13.54% (98/724) isolated PubChem CIDs; remainder under Valid_Missing_Ethnomedical.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 3: TDA BENCHMARK
# ==============================================================================
with tab_tda:
    st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
    t_c1, t_c2 = st.columns([1.5, 1.0])
    with t_c1:
        st.markdown("<b>Table 1: Comparative Geometric Dimensionality Reduction (99.39% Sparsity)</b>", unsafe_allow_html=True)
        st.dataframe(df_t1, use_container_width=True, height=260)
    with t_c2:
        st.markdown(f"""
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:10px; font-size:0.78rem; line-height:1.6;">
            <b>🔬 Persistent Simplicial Invariants</b><br>
            • <b>H₀ Clusters:</b> 211 Persistent Features (Entropy: 0.9966)<br>
            • <b>H₁ Synergy Loops:</b> 13 Invariant Cavities (Entropy: 0.9264)<br>
            • <b>Filtration Interval:</b> Invariant over ε ∈ [0.80, 0.99]<br>
            <hr style="margin:4px 0;">
            <b>🌐 Bottleneck Alignment vs Canonical TCM</b><br>
            • <b>d_B(H₁) = 0.0435:</b> Strictly conserved higher-order synergy loops<br>
            • <b>d_B(H₀) = 0.2500:</b> Biogeographical tropical flora speciation<br>
            <span style="color:#059669; font-weight:600;">Proves mathematical structural equivalence between VTM and canonical Asian pharmacopoeias.</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 4: HGNN BENCHMARK
# ==============================================================================
with tab_hgnn:
    st.markdown('<div class="exec-panel">', unsafe_allow_html=True)
    h_c1, h_c2 = st.columns([1.3, 1.0])
    with h_c1:
        st.markdown("<b>Table 2: Link Prediction Benchmark (Hold-out Test Set N=106, 80/20 Edge Split)</b>", unsafe_allow_html=True)
        st.dataframe(df_t2, use_container_width=True, height=140)
    with h_c2:
        st.markdown("""
        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-left:3px solid #16A34A; border-radius:6px; padding:10px; font-size:0.78rem; line-height:1.6;">
            <b style="color:#16A34A;">Model Evaluation Summary</b><br>
            • <b>Topological HGNN (Ours):</b> AUC-ROC = <b>1.0000</b> | AP = <b>1.0000</b><br>
            • <b>Pairwise Baseline (GCN):</b> AUC-ROC = <b>0.8270</b> | AP = <b>0.8302</b><br>
            • <b>Relative Gain:</b> <b>+17.30%</b> under 99.39% matrix sparsity.<br>
            <div style="font-size:0.72rem; color:#475569; margin-top:4px;">Simplicial boundary operators prevent Laplacian oversmoothing over sparse bipartite structures.</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
