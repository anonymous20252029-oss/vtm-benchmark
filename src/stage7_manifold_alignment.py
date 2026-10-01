"""Stage 7: Empirical Cross-System Manifold Alignment via Bottleneck Distance."""
import gudhi.bottleneck
import numpy as np

def compute_cross_system_bottleneck(diag_vtm_h0, diag_vtm_h1, diag_tcm_h0, diag_tcm_h1):
    d_b_h0 = gudhi.bottleneck_distance(diag_vtm_h0, diag_tcm_h0)
    d_b_h1 = gudhi.bottleneck_distance(diag_vtm_h1, diag_tcm_h1) if len(diag_vtm_h1) > 0 else 0.0
    return d_b_h0, d_b_h1