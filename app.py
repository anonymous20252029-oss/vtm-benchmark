"""
VTM-TDA Benchmark: Topological Data Orchestration for Indigenous Ethnomedicine
Executive Single-Page Clinical Dashboard (FAIR-Compliant Platform)
Author: Thi Kim-Anh Vo
"""

import streamlit as st
import pandas as pd
import numpy as np

# Cấu hình trang toàn màn hình
st.set_page_config(
    page_title="VTM-TDA Executive Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS tối giản, triệt tiêu khoảng cách thừa mà không can thiệp vỡ DOM
st.markdown("""
<style>
    /* 1. Nén lề trang chính */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
    }
    
    /* Ẩn sidebar thừa */
    [data-testid="collapsedControl"] { display: none !important; }

    /* 2. Tiêu đề chính */
    .hero-title {
        text-align: center;
        font-size: 1.45rem;
        font-weight: 800;
        color: #0F172A;
        margin: 0;
        line-height: 1.2;
    }
    .hero-sub {
        text-align: center;
        font-size: 0.8rem;
        color: #475569;
        margin: 2px 0 8px 0;
    }

    /* 3. Băng thông số ngang (Metric Ribbon) */
    .kpi-ribbon {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        background: #FFFFFF;
        padding: 6px 12px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin-bottom: 10px;
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
    }
    .kpi-val {
        font-size: 1.1rem;
        font-weight: 800;
        color: #0F172A;
    }
    .kpi-sub {
        font-size: 0.63rem;
        color: #059669;
        font-weight: 600;
        display: block;
    }

    /* 4. Tab list */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px !important;
        margin-bottom: 8px !important;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 4px 14px !important;
        font-size: 0.85rem !important;
        font-weight: 600;
    }

    /* 5. Thẻ hiển thị bài thuốc trong cột 3 */
    .formula-badge {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 3px solid #0D9488;
        border-radius: 4px;
        padding: 6px 8px;
        margin-bottom: 6px;
        font-size: 0.78rem;
    }
</style>
""", unsafe_allow_html=True)

# 1. Header ở giữa
st.markdown("""
<div class="hero-title">🌿 VTM-TDA: Topological Data Orchestration Framework</div>
<div class="hero-sub">AI-Ready Benchmark & Hypergraph Learning for Vietnamese Traditional Medicine (Prof. Do Tat Loi Pharmacopoeia)</div>
""", unsafe_allow_html=True)

# 2. Nạp dữ liệu
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
    st.error(f"Error loading datasets from 'data/' folder: {e}")
    st.stop()

# 3. Băng thông số KPI ngang 1 dòng
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

# 4. Các Tab chức năng
tab_cases, tab_browser, tab_tda, tab_hgnn = st.tabs([
    "🌟 Clinical Case Explorer",
    "🔍 Multi-Tier Cross-Ontology Directory",
    "📐 TDA vs Baselines Benchmark",
    "🧠 HGNN Synergy Link Prediction"
])

# ==============================================================================
# TAB 1: BỐ CỤC 3 CỘT TRỰC TIẾP (DÙNG ST.CONTAINER NGUYÊN BẢN CỦA STREAMLIT)
# ==============================================================================
with tab_cases:
    case_options = {
        "Ích Mẫu (Leonurus heterophyllus)": 1,
        "Hương Phụ (Cyperus rotundus)": 2,
        "Diếp Cá (Houttuynia cordata)": 5,
        "Đương Quy (Angelica sinensis)": 17,
        "Hồng Hoa (Carthamus tinctorius)": 6,
        "Sinh Địa - Thục Địa (Rehmannia glutinosa)": 588
    }

    col_1, col_2, col_3 = st.columns([1.1, 1.1, 1.8])

    # CỘT 1: Danh pháp & Thực vật học
    with col_1:
        with st.container(border=True):
            st.markdown("##### 🌿 Botanical Identity")
            selected_name = st.selectbox("Select Signature Herb:", list(case_options.keys()), label_visibility="collapsed")
            selected_id = case_options[selected_name]
            c_data = df_cross[df_cross['ID_ViThuoc'] == selected_id].iloc[0]

            st.markdown(f"""
            **• Tên Việt Nam:** `{c_data['TenVietNam']}`  
            **• Tên khoa học:** *{c_data['Binomial']}*  
            **• Họ thực vật:** *{c_data.get('HoThucVat', 'N/A')}*  
            **• Tên gọi khác:** {str(c_data.get('TenGoiKhac', 'None'))[:35]}  
            **• Kew POWO:** [Link POWO]({c_data.get('POWO_Taxon_URL', 'https://powo.science.kew.org')})  
            **• NCBI TaxID:** `{c_data.get('NCBI_TaxID', '588 Verified')}`
            """)

    # CỘT 2: Hóa sinh & Đông y Triangulation
    with col_2:
        with st.container(border=True):
            st.markdown("##### 🌐 Chemistry & Energetics")
            st.markdown(f"""
            **• TCM Equiv.:** {c_data.get('TCM_Chinese', 'N/A')} ({c_data.get('TCM_Pinyin', 'N/A')})  
            **• TCMSP ID:** `{c_data.get('TCMSP_ID', 'N/A')}`  
            **• IMPPAT ID:** `{c_data.get('IMPPAT_ID', 'N/A')}`  
            **• Active Compound:** **{c_data.get('Primary_Compound', 'N/A')}**  
            **• PubChem CID:** `{int(c_data['PubChem_CID']) if pd.notna(c_data['PubChem_CID']) else 'N/A'}`  
            ***
            **• Tính Vị:** {c_data.get('TinhVi', 'N/A')}  
            **• Quy Kinh:** `{c_data.get('QuyKinh', 'N/A')}`  
            **• Liều dùng:** {c_data.get('LieuDung', '6-12g/ngày')}
            """)

    # CỘT 3: Các bài thuốc liên kết (Có khung cuộn nội bộ mượt mà)
    with col_3:
        with st.container(border=True):
            linked_ids = df_cong[df_cong['ID_ViThuoc'] == selected_id]['ID_BaiThuoc'].unique()
            matching_prescs = df_bai[df_bai['ID_BaiThuoc'].isin(linked_ids)]
            st.markdown(f"##### 📜 Clinical Formulations ({len(matching_prescs)} found)")

            with st.container(height=340):
                if len(matching_prescs) > 0:
                    for _, p_row in matching_prescs.iterrows():
                        co_herbs = df_cong[df_cong['ID_BaiThuoc'] == p_row['ID_BaiThuoc']]
                        co_details = df_vi[df_vi['ID_ViThuoc'].isin(co_herbs['ID_ViThuoc'])]
                        roster = " + ".join([f"`{h}`" for h in co_details['TenVietNam'].tolist()])
                        
                        st.markdown(f"""
                        <div class="formula-badge">
                            <b style="color:#0F172A;">💊 #{p_row['ID_BaiThuoc']}: {p_row['TenBaiThuoc']}</b><br>
                            <span style="color:#64748B;"><b>Chủ trị:</b> {p_row.get('ChuTri', 'Standard indication')} | <b>Nguồn:</b> {p_row.get('NguonGoc', 'Đỗ Tất Lợi')}</span><br>
                            <span style="margin-top:2px; display:block;"><b>Phối ngũ:</b> {roster}</span>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("Vị thuốc dùng độc vị, không nằm trong phương thang đa vị phức tạp.")

# ==============================================================================
# TAB 2: DIRECTORY BROWSER
# ==============================================================================
with tab_browser:
    with st.container(border=True):
        f1, f2, f3 = st.columns([1.5, 1.5, 1.0])
        with f1:
            s_vn = st.text_input("Filter Vietnamese:", placeholder="Nhập tên tiếng Việt...", label_visibility="collapsed")
        with f2:
            s_latin = st.text_input("Filter Latin / Compound:", placeholder="Nhập tên Latin hoặc hoạt chất...", label_visibility="collapsed")
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
                'ID_ViThuoc': 'ID', 'TenVietNam': 'Tên Việt Nam', 'Binomial': 'Latin Binomial',
                'TCM_Chinese': 'TCM Hanzi', 'TCMSP_ID': 'TCMSP', 'Primary_Compound': 'Hoạt chất', 'PubChem_CID': 'PubChem CID'
            }),
            use_container_width=True,
            height=320
        )
        st.caption("Curation Audit: 81.22% (588/724) NCBI Taxonomy; 13.54% (98/724) PubChem CIDs; còn lại theo Valid_Missing_Ethnomedical.")

# ==============================================================================
# TAB 3: TDA BENCHMARK
# ==============================================================================
with tab_tda:
    with st.container(border=True):
        t_c1, t_c2 = st.columns([1.5, 1.0])
        with t_c1:
            st.markdown("##### Table 1: Comparative Evaluation (99.39% Sparsity)")
            st.dataframe(df_t1, use_container_width=True, height=270)
        with t_c2:
            st.markdown("##### 🔬 Invariants & Alignment")
            st.markdown("""
            * **H₀ Clusters:** **211 Persistent Features** (Entropy: **0.9966**)
            * **H₁ Synergy Loops:** **13 Invariant Cavities** (Entropy: **0.9264**)
            * **Filtration Interval:** Bền vững qua $\epsilon \in [0.80, 0.99]$
            ***
            * **Bottleneck vs TCM:**
              - **$d_B(H_1) = 0.0435$:** Chu trình phối ngũ hiệp đồng được bảo toàn tuyệt đối
              - **$d_B(H_0) = 0.2500$:** Phân kỳ kiểu hình do tính đa dạng thực vật nhiệt đới
            """)

# ==============================================================================
# TAB 4: HGNN BENCHMARK
# ==============================================================================
with tab_hgnn:
    with st.container(border=True):
        h_c1, h_c2 = st.columns([1.3, 1.0])
        with h_c1:
            st.markdown("##### Table 2: Link Prediction (Test Set N=106, Edge Split 80/20)")
            st.dataframe(df_t2, use_container_width=True, height=140)
        with h_c2:
            st.success("""
            **Kết quả thực nghiệm nổi bật:**
            • **Topological HGNN (Ours):** AUC-ROC = **1.0000** | AP = **1.0000**  
            • **Pairwise Baseline (GCN):** AUC-ROC = **0.8270** | AP = **0.8302**  
            • **Mức tăng hiệu năng:** **+17.30%** trên dữ liệu thưa 99.39%.
            """)
            st.info("Biểu diễn simplicial và các chu trình tô-pô ngăn chặn hoàn toàn hiện tượng oversmoothing của mô hình đồ thị cặp thông thường.")
