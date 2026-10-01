"""Stage 1: Fault-Tolerant Streaming OCR Engine with Disk Checkpointing."""
import os, json, time
import pytesseract
from pdf2image import convert_from_path

def run_stage1_streaming_ocr(pdf_path, checkpoint_dir, start_page=30, total_pages=1050, batch_size=20):
    os.makedirs(checkpoint_dir, exist_ok=True)
    status_file = os.path.join(checkpoint_dir, "ocr_checkpoint_status.json")
    
    current_page = start_page
    if os.path.exists(status_file):
        with open(status_file, "r", encoding="utf-8") as f:
            current_page = json.load(f).get("last_processed_page", start_page) + 1

    print(f"[Stage 1] Ingesting scanned monographs from page {current_page} to {total_pages}...")
    for p_start in range(current_page, total_pages + 1, batch_size):
        p_end = min(p_start + batch_size - 1, total_pages)
        t0 = time.time()
        images = convert_from_path(pdf_path, first_page=p_start, last_page=p_end, dpi=150)
        
        batch_text = {}
        for idx, img in enumerate(images):
            page_num = p_start + idx
            batch_text[page_num] = pytesseract.image_to_string(img, lang="vie")
            
        with open(status_file, "w", encoding="utf-8") as f:
            json.dump({"last_processed_page": p_end, "timestamp": time.ctime()}, f, indent=2)
        print(f" -> Batch {p_start}-{p_end} completed in {time.time()-t0:.1f}s.")