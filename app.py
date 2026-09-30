import streamlit as st
import pandas as pd
import numpy as np

# Cấu hình giao diện trang
st.set_page_config(
    page_title="VTM-TDA Benchmark | CSBJ Demo",
    page_icon="🌿",
    layout="wide"
)

# Header
st.title("🌿 VTM-TDA: Topological Data Orchestration for Vietnamese Ethnomedicine")
st.markdown("""
**Interactive Demonstration Platform for Paper 1** (CSBJ Special Issue on *Data Orchestration*)  
*Author: Anh Thi-Kim Vo (VŠB - Technical University of Ostrava)*
""")

# Load dữ liệu từ thư mục data/
@st.cache_data
def load_data():
    df_vi = pd.read_csv("data/ViThuoc_Master_Harmonized.csv")
    df_bai = pd.read_csv("data/BaiThuoc_Master_Harmonized.csv")
    df_cross = pd.read_csv("data/ViThuoc_Global_CrossOntology_Master.csv")
    df_t1 = pd.read_csv("data/Table1_Comparative_Topological_Benchmark.csv")
    df_t2 = pd.read_csv("data/Table2_HGNN_Synergy_Prediction_Benchmark.csv")
    return df_vi, df_bai, df_cross, df_t1, df_t2

df_vi, df_bai, df_cross, df_t1, df_t2 = load_data()

# Sidebar: Thống kê tổng quan
st.sidebar.header("📊 Benchmark Overview")
st.sidebar.metric("Master Botanical Taxa", len(df_vi))
st.sidebar.metric("Validated Formulations", len(df_bai))
st.sidebar.metric("Hypergraph Sparsity", "99.39%")
st.sidebar.metric("Bottleneck Distance (dB)", "0.0926")

# Chia Tab chức năng
tab1, tab2, tab3 = st.tabs([
    "🔍 Multi-Tier Entity Browser", 
    "📈 Topological vs Classical Benchmark", 
    "🧠 HGNN Synergy Prediction"
])

# Tab 1: Tra cứu thực thể vị thuốc & Cross-Ontology
with tab1:
    st.subheader("1. Cross-Ontology Alignment Browser")
    col1, col2 = st.columns([1, 2])
    with col1:
        search_kw = st.text_input("Tìm kiếm theo tên vị thuốc:", "Ích Mẫu")
        filtered = df_cross[df_cross['TenVietNam'].str.contains(search_kw, case=False, na=False)]
    with col2:
        if len(filtered) > 0:
            row = filtered.iloc[0]
            st.success(f"**Vị thuốc:** {row['TenVietNam']}")
            st.write(f"- **Tên khoa học (POWO):** *{row.get('Binomial', 'N/A')}*")
            st.write(f"- **TCM Chinese:** {row.get('TCM_Chinese', 'N/A')} | **TCMSP ID:** `{row.get('TCMSP_ID', 'N/A')}`")
            st.write(f"- **Hoạt chất chính:** {row.get('Primary_Compound', 'N/A')} (PubChem CID: `{row.get('PubChem_CID', 'N/A')}`)")
            st.write(f"- **IMPPAT ID:** `{row.get('IMPPAT_ID', 'N/A')}`")
        else:
            st.warning("Không tìm thấy kết quả phù hợp.")
    
    st.write("---")
    st.dataframe(filtered[['ID_ViThuoc', 'TenVietNam', 'Binomial', 'TCM_Chinese', 'TCMSP_ID', 'Primary_Compound', 'PubChem_CID']], use_container_width=True)

# Tab 2: So sánh TDA vs Baseline
with tab2:
    st.subheader("2. Quantitative Comparative Evaluation Under 99.39% Sparsity")
    st.markdown("So sánh hiệu năng giữa phép chiếu phẳng (PCA, t-SNE) và Không gian Simplicial Homology:")
    st.dataframe(df_t1, use_container_width=True)

# Tab 3: Kết quả mô hình HGNN
with tab3:
    st.subheader("3. Downstream Herb-Herb Synergy Link Prediction")
    st.markdown("Hiệu năng mô hình Topological Hypergraph Neural Network (HGNN) trên 1.060 cặp thử nghiệm:")
    st.dataframe(df_t2, use_container_width=True)
