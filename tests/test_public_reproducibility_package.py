from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist() -> None:
    required = [
        "README.md",
        "DATA_NOTICE.md",
        "CITATION.cff",
        "LICENSE",
        "requirements.txt",
        "paper18_submission_source/main.tex",
        "paper18_submission_source/refs.bib",
        "paper18_submission_source/main.pdf",
        "arxiv_submission_source.zip",
        "scripts/reproduce.py",
        "scripts/build_mar_summary.py",
        "scripts/build_figures.py",
        "scripts/build_arxiv_source.py",
        "data/derived/mar_toy_model_results.csv",
        "data/derived/mar_realistic_stress_test_results.csv",
        "data/derived/mar_systematics_separation_results.csv",
        "data/derived/mar_v2_current_scores.csv",
        "data/derived/mar_b1c_oos_scale_validation_aggregate.csv",
        "data/derived/mar_b1d2_physical_shear_aggregate.csv",
        "data/derived/mar_b1e_null_matter_link_results.csv",
        "data/derived/paper18_mar_summary.csv",
        "figures/fig_mar_protocol.pdf",
        "figures/fig_mar_sensitivity_ladder.pdf",
        "figures/fig_mar_stress_summary.pdf",
        "figures/fig_mar_delta_r2_after_controls.pdf",
        "figures/fig_mar_v2_scorecard.pdf",
        "figures/fig_mar_b1c_oos_scale_validation.pdf",
        "figures/fig_mar_b1d2_physical_shear.pdf",
        "figures/fig_mar_b1e_null_matter_link.pdf",
    ]
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    assert not missing, missing


def test_claim_boundaries_are_explicit() -> None:
    text = (
        (ROOT / "README.md").read_text(encoding="utf-8")
        + "\n"
        + (ROOT / "paper18_submission_source" / "main.tex").read_text(encoding="utf-8")
    )
    forbidden = [
        "we prove Tau Core",
        "Tau Core is validated",
        "we falsify dark matter",
        "dark matter is solved",
        "we report empirical discovery",
    ]
    for phrase in forbidden:
        assert phrase not in text
    for phrase in [
        "synthetic methodology",
        "not empirical",
        "not physical validation",
        "does not prove Tau Core",
        "does not analyze real survey data",
        "CONTROLLED_SYNTHETIC_MOCK_PHOTON_LENSING_MAR_V2_PROTOCOL",
        "Q_{\\rm MAR}=13/24",
        "not observational evidence",
    ]:
        assert phrase in text


def test_summary_values() -> None:
    payload = json.loads((ROOT / "data" / "derived" / "paper18_mar_summary.json").read_text())
    assert payload["claim_boundary"] == "controlled_synthetic_mock_protocol_not_observational_evidence"
    assert abs(payload["toy_c_tau"] - 0.874517) < 1e-6
    assert abs(payload["toy_spatial_shuffle_mean"] - 0.012301) < 1e-6
    assert payload["stress_mild_q_mar_0_to_10"] == 5
    assert payload["stress_no_tau_control_medium_q_mar_0_to_10"] == 2
    assert payload["systematics_no_tau_control_medium_delta_r2_tau_after_controls"] < 1e-5
    assert payload["mar_v2_score_total"] == 13
    assert payload["mar_v2_score_max"] == 24
    assert abs(payload["b1d2_kappa_delta_r2_mean"] - 0.0656411544952686) < 1e-10
    assert abs(payload["b1e_lensing_residual_after_matter_transfer_delta_r2"] - 0.0995491707671321) < 1e-10
    assert abs(payload["b1e_lensing_residual_after_matter_transfer_partial_corr"] - 0.2644538134099959) < 1e-10


def test_summary_csv_contains_claim_metrics() -> None:
    rows = {}
    with (ROOT / "data" / "derived" / "paper18_mar_summary.csv").open(
        newline="", encoding="utf-8"
    ) as f:
        for row in csv.DictReader(f):
            rows[row["metric"]] = row["value"]
    assert float(rows["toy_c_tau"]) > float(rows["toy_random_orientation_mean"])
    assert float(rows["stress_hard_q_mar_0_to_10"]) == 4
    assert float(rows["systematics_mild_delta_r2_tau_after_controls"]) > 0
    assert float(rows["mar_v2_score_fraction"]) > 0.5
    assert float(rows["b1c_best_tau_injected_delta_r2_mean"]) > 0
    assert float(rows["b1e_matter_dynamics_residual_controls_delta_r2"]) < 0


def test_arxiv_zip_is_source_only() -> None:
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = set(zf.namelist())
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    assert "figures/fig_mar_protocol.pdf" in names
    assert "figures/fig_mar_stress_summary.pdf" in names
    assert "figures/fig_mar_v2_scorecard.pdf" in names
    assert "figures/fig_mar_b1e_null_matter_link.pdf" in names
