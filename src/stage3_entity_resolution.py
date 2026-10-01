"""Stage 2: Semantic NLP Parsing and Historical Section A–E Segmentation."""
import re
import pandas as pd

def parse_section_structures(page_text_dict):
    prescriptions, formulas, chemicals = [], [], []
    for page_num, txt in page_text_dict.items():
        # Parse Section E (Prescriptions and herb dosages)
        matches = re.findall(r'(?:Đơn thuốc|Bài thuốc|Chữa)\s+([^:\n\.]+):?\s*([^.\n]+(?:g|gam|đồng cân|lát|quả)[^.\n]+)', txt, re.I)
        for title, f_str in matches:
            presc_id = f"BT_P{page_num}_{abs(hash(title)) % 10000}"
            prescriptions.append({"ID_BaiThuoc_OCR": presc_id, "TenBaiThuoc": title.strip(), "Trang": page_num})
            for ing in re.split(r'[,;]', f_str):
                dose_m = re.search(r'(\d+[\.,]?\d*)\s*(g|gam|đồng cân|quả|lát)', ing, re.I)
                dose = dose_m.group(0) if dose_m else "Theo kinh nghiệm"
                ing_cl = re.sub(r'(\d+[\.,]?\d*)\s*(g|gam|đồng cân|quả|lát)|\(.*?\)', '', ing).strip()
                if len(ing_cl) > 1:
                    formulas.append({"ID_BaiThuoc_OCR": presc_id, "TenViThuoc": ing_cl, "LieuLuong": dose})
                    
        # Parse Section C (Phytochemical constituents)
        chem_match = re.search(r'C\.\s*Thành phần hoá học(.*?)(?=D\.\s*Tác dụng|E\.\s*Công dụng|\Z)', txt, re.S | re.I)
        if chem_match:
            compounds = re.findall(r'\b([A-Za-z0-9_\-]+(?:in|ol|en|on|oside|ozit|genin))\b', chem_match.group(1))
            chemicals.append({"Trang": page_num, "HoatChat": "; ".join(set(compounds))})

    return pd.DataFrame(prescriptions), pd.DataFrame(formulas), pd.DataFrame(chemicals)