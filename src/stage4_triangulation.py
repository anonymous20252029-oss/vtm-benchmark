"""Stage 4: Hierarchical Knowledge Triangulation and FAIR Provenance Flagging."""
import pandas as pd
import numpy as np

def apply_hierarchical_triangulation(df_vi, global_ontology_dict):
    df_vi['NCBI_TaxID_Match'] = False
    df_vi['PubChem_CID'] = np.nan
    df_vi['Provenance_Flag'] = "Valid_Missing_Ethnomedical"

    for idx, r in df_vi.iterrows():
        b_name = r.get('Binomial', '')
        if b_name in global_ontology_dict:
            meta = global_ontology_dict[b_name]
            df_vi.at[idx, 'TCM_Chinese'] = meta.get('TCM_Chinese')
            df_vi.at[idx, 'TCMSP_ID'] = meta.get('TCMSP_ID')
            df_vi.at[idx, 'Primary_Compound'] = meta.get('Primary_Compound')
            df_vi.at[idx, 'PubChem_CID'] = meta.get('PubChem_CID')
            df_vi.at[idx, 'NCBI_TaxID_Match'] = True
            df_vi.at[idx, 'Provenance_Flag'] = "Cross_Database_TCMSP"

    # Gán nhãn cho các chuyên khảo đã thẩm định DĐVN V
    df_vi.loc[df_vi['TinhVi'].notna(), 'Provenance_Flag'] = "DDVN_V_Concordant"
    return df_vi