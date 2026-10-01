"""Stage 10: Open-Science FAIR Metadata Serialization."""
import json

def generate_zenodo_fair_metadata(out_path):
    meta = {
        "title": "A FAIR Topological Data Orchestration Benchmark for Vietnamese Traditional Medicine (VTM)",
        "upload_type": "dataset",
        "access_right": "open",
        "license": "CC-BY-4.0",
        "doi": "10.5281/zenodo.23075404",
        "keywords": ["Topological Data Analysis", "Persistent Homology", "Hypergraph Learning", "FAIR Benchmark"]
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)